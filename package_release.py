#!/usr/bin/env python3
"""Validate and package Emlékőr without signing material or personal journals."""
from pathlib import Path
import os,json,zipfile,hashlib,subprocess
ROOT=Path(__file__).resolve().parent
OUT=ROOT.parent/'deliverables';OUT.mkdir(exist_ok=True)
VERSION='1.1.0';PREFIX='Emlekor-'+VERSION
apk=ROOT/'dist'/(PREFIX+'.apk')
bt=Path(os.environ['ANDROID_HOME'])/'build-tools/35.0.0'
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def certificate(path):
    out=subprocess.check_output([str(bt/'apksigner'),'verify','--print-certs',str(path)],text=True)
    return next(line.split(': ',1)[1] for line in out.splitlines() if 'certificate SHA-256 digest:' in line)
with zipfile.ZipFile(apk) as archive:
    assert archive.testzip() is None
    assets=[p for p in (ROOT/'app/src/main/assets').rglob('*') if p.is_file()]
    for p in assets:assert archive.read('assets/'+p.relative_to(ROOT/'app/src/main/assets').as_posix())==p.read_bytes()
cert=certificate(apk)
previous=os.environ.get('PREVIOUS_APK')
if previous:assert certificate(Path(previous))==cert,'Original signing certificate changed'
badging=subprocess.check_output([str(bt/'aapt2'),'dump','badging',str(apk)],text=True)
assert "package: name='hu.emlekor.naplo'" in badging
assert "versionCode='2'" in badging and "versionName='1.1.0'" in badging
assert "minSdkVersion:'26'" in badging and 'uses-permission:' not in badging
reports={name:json.loads((ROOT/'qa'/name).read_text()) for name in ['test-results.json','offline-results.json','growth-results.json']}
for name,data in reports.items():
    assert not data.get('errors') and not data.get('network') and not data.get('requests')
    (ROOT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2))
count=sum(data['passed'] for data in reports.values())
validation={'version':VERSION,'package':'hu.emlekor.naplo','versionCode':2,'sha256':digest(apk),'certificateSHA256':cert,'sameCertificateAsPrevious':True if previous else None,'zipIntegrity':True,'assetCount':len(assets),'allAssetsMatch':True,'androidPermissions':[],'automatedChecks':count,'physicalPhoneTest':False}
(ROOT/'apk-validation.json').write_text(json.dumps(validation,indent=2))
(ROOT/'VALIDATION.md').write_text(f'''# Emlékőr 1.1.0 – ellenőrzés

2026. november 5. **{count} sikeres automatizált ellenőrzés.**

| Csoport | Ellenőrzés |
|---|---:|
| Napló, adattár, Java/WebCrypto és hibaágak | {reports['test-results.json']['passed']} |
| Offline, éles felület és jelszavas fájlexport | {reports['offline-results.json']['passed']} |
| Új grafika, kert, ösvények, albumok és migráció | {reports['growth-results.json']['passed']} |

- Valós űrlapkitöltés és mentés; piszkozat-újranyitás, keresés, kedvencek, törlés.
- Java és WebCrypto között bájtra azonos jelszavas mentés-visszatöltés; hibás jelszó
  és módosított ciphertext elutasítása. A Java segéd valódi JVM-ben futott.
- Ismételt import duplikálás nélkül; eltérő változatok és helyi piszkozat megtartása.
- Natív bridge-szimuláció, olvashatatlan tár felülírásának tiltása és mentési hiba jelzése.
- Nyolc ösvény, hat album, tizenkét jelvény, négy kert és hat növekedési kép.
- Ösvény indítása nem ír eseményt a felhasználó helyett és nem címkéz át régi piszkozatot.
- A nehéz emlék is számít; az aznapi többszöri mentés nem szaporítja a 10 levelet.
- Régi 1.0-s formátum megőrzi a szöveget és a beállításokat; a hiányzó kertválasztás
  alapértéket kap. Nem egymás utáni írásnapok is feloldják a kertet.
- Kertválasztás túléli az újranyitást és a titkosított exportot. Ismételt import nem ad újabb jutalmat.
- Album az eredeti bejegyzéseket szűri, nem készít másolatokat. Törléskor a haladás újraszámolódik.
- 320×568, 390×844, 412×915 és 800×600 kijelzők, főnézetek és nagy betűk,
  vízszintes túlcsordulás nélkül. A főoldalt és kertet vizuálisan is átnéztük.
- Csökkentett mozgás figyelembevétele; tesztfelület éles módban nem érhető el.
- Nincs külső hálózati kérés vagy JavaScript-hiba.

## APK és forrás

V2/v3 aláírás érvényes, ZIP sértetlen, az összes ({len(assets)}) beágyazott webes asset
bájtra egyezik a forrással. Csomag hu.emlekor.naplo, verzió 1.1.0 / 2,
minSdk 26, targetSdk 35. Nincs kért Android-engedély, hálózati engedély sem.
A tanúsítvány{' egyezik az 1.0.0 APK-val' if previous else ' összevetéséhez PREVIOUS_APK megadása szükséges'}.
Méret: {apk.stat().st_size} bájt. SHA-256: `{digest(apk)}`.

A forráscsomagban nincs signing mappa, jelszó, személyes napló, mentésfájl,
QA-kép vagy buildkönyvtár. A kulcs külön privát ZIP-ben marad.
A natív adattárolási és kriptográfiai Java-fájlok változatlanok az 1.0-s kiadáshoz képest.

## A vizsgálat határa

**Fizikai Android-telefonos teszt nem történt.** A Keystore, AtomicFile,
rendszermegosztás, dokumentumválasztó, képernyőbillentyűzet és akadálymentes
felolvasás működését konkrét telefonon is ellenőrizni kell. A böngészős bridge-szimuláció
nem helyettesíti a natív integrációs próbát; Androidos biztonsági minősítés nem történt.
''')
def atomic_copy(source,target):
    temp=target.with_suffix(target.suffix+'.pending')
    with temp.open('wb') as stream:stream.write(source.read_bytes());stream.flush();os.fsync(stream.fileno())
    os.replace(temp,target)
for source,target in [(apk,OUT/apk.name),(ROOT/'PROJECT_HANDOFF.md',OUT/'Emlekor-Codex-atadas.md'),(ROOT/'CHANGELOG.md',OUT/'Emlekor-1.1.0-valtozasnaplo.md')]:atomic_copy(source,target)
files=[]
for folder in ['app','tests']:
    files.extend(p for p in (ROOT/folder).rglob('*') if p.is_file() and 'build' not in p.relative_to(ROOT).parts)
for pattern in ['*.md','*.py','*.json','.gitignore','.gitattributes']:files.extend(ROOT.glob(pattern))
forbidden={'.jks','.keystore','.p12','.pfx','.pem','.apk','.aab','.emlekor','.pyc'}
files=[p for p in sorted(set(files)) if p.suffix.lower() not in forbidden]
archive=OUT/(PREFIX+'-forraskod.zip');temp=archive.with_suffix('.zip.pending')
with zipfile.ZipFile(temp,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:z.write(p,PREFIX+'/'+p.relative_to(ROOT).as_posix())
with zipfile.ZipFile(temp) as z:
    assert z.testzip() is None
    for n in z.namelist():
        assert Path(n).suffix.lower() not in forbidden
        assert not any(part in {'signing','qa','build','node_modules','.git'} for part in Path(n).parts)
    for p in files:assert z.read(PREFIX+'/'+p.relative_to(ROOT).as_posix())==p.read_bytes()
os.replace(temp,archive)
outputs=[OUT/apk.name,archive,OUT/'Emlekor-Codex-atadas.md',OUT/'Emlekor-1.1.0-valtozasnaplo.md']
(OUT/(PREFIX+'-SHA256SUMS.txt')).write_text(''.join(digest(p)+'  '+p.name+'\n' for p in outputs))
for p in outputs:print(p.name,p.stat().st_size,digest(p))
print('Verified checks:',count)
