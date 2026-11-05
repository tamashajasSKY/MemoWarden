# Emlékőr 1.1.0

## Letöltés és telepítés

### [⬇ Emlékőr 1.1.0 APK letöltése](https://github.com/tamashajasSKY/MemoWarden/releases/download/v1.1.0/Emlekor-1.1.0.apk)

**Android 8.0 vagy újabb · magyar nyelv · offline használat**

[Forráscsomag](https://github.com/tamashajasSKY/MemoWarden/releases/download/v1.1.0/Emlekor-1.1.0-forraskod.zip) · [GitHub-kiadások](https://github.com/tamashajasSKY/MemoWarden/releases) · [Telepítési útmutató](docs/TELEPITES.md) · [Adatkezelés](docs/ADATKEZELES.md)

1. Töltsd le az APK-t a telefonodra, és nyisd meg a letöltött fájlt.
2. Ha Android kéri, engedélyezd a használt böngészőnek vagy fájlkezelőnek az alkalmazástelepítést.
3. Válaszd a **Telepítés**, majd a **Megnyitás** lehetőséget.

Frissítés előtt készíts jelszavas mentést. A régi alkalmazást ne távolítsd el: ezzel a helyi napló is elveszhet. Meglévő telepítés csak egyező aláírással frissíthető. Fizikai Android-telefonos ellenőrzés még nem történt; a részletek a [VALIDATION.md](VALIDATION.md) fájlban olvashatók.

APK-méret: **54 369 bájt**. SHA-256:

```text
e71de1b76217dd9937ed3db40ac6f3a9ad79e55e92840f6babb354dd13e40a99
```

Mindkét eredeti fájl ellenőrzőösszege: [SHA256SUMS](SHA256SUMS). Linuxon: `sha256sum -c SHA256SUMS`.

## Az alkalmazásról

Magyar, offline emléknapló Androidra. **Értéket teremtünk. Emlékeket védünk.**
Napi pár perces, vezetett írás gyerekekkel közös használathoz, felnőtteknek és idősebbeknek.
Android 8.0+ (minSdk 26), csomagnév `hu.emlekor.naplo`. A régi Emlékőrre frissítésként telepíthető
az eredeti aláírókulccsal; az alkalmazást ne távolítsd el előtte.

## Az új verzió

- Saját rajzolt emlékkönyv, részletesen növekvő kert, képes naplókártyák és hangulatok.
- Nyolc választható emlékösvény, ösvényenként három valódi emlékkel.
- Hat automatikus emlékalbum és tizenkét képes jelvény.
- Négy kert: tisztás, alkony, csillagliget és ősz; 0/30/70/150 emléklevélnél választhatók.
- Egy külön írással töltött nap 10 levelet ad. Nincs elkölthető egyenleg, elvesző sorozat vagy időkorlát.
- A hangulatválasztás nem módosítja a jutalmat: a nehéz emlék is ugyanúgy számít.

A háromlépéses naplóírás, piszkozatmentés, segítő kérdések, kulcsszavak, keresés, kedvencek,
visszaolvasás, szerkesztés és nagyobb betűméret megmarad. A szövegrendezés csak a megadott
részleteket használja, eseményt vagy érzést nem talál ki.

## Mentés

Androidon a napló az alkalmazás privát tárában, Keystore-kulccsal titkosítva tárolódik.
**Beállítások → Jelszavas biztonsági másolat** készít hordozható `.emlekor` fájlt.
Másik telefonon: **Mentés visszatöltése**, fájl és jelszó megadása, majd megerősítés.

A meglévő emlékek megmaradnak; az eltérő változatok külön bejegyzésként őrződnek meg,
az azonosak nem duplázódnak. Az import nem ad újabb pontot ugyanazokért az emlékekért.
A jelszó nem állítható helyre. A helyi titkosítás mellett is készíts külön másolatot:
eltávolításkor vagy a telefon elvesztésekor a helyi adattár is elveszhet.
A régi, 1.0-s mentések beolvashatók. A piszkozat és a napló mentési formátuma nem változott.

## A saját tempódban

Az ösvény a kezdéskor egy eltávolítható kulcsszót tesz az emlékhez. E jelölés alapján számolja
az ösvény haladását, nem elemzi és nem pontozza a személyes történet tartalmát.
Az albumok kulcsszavas nézetek, ugyanaz az emlék több albumban is megjelenhet. A haladás
az aktuálisan meglévő emlékekből számolódik, ezért törlés után újraszámolódik.

## Fejlesztés és átadás

A MemoWarden repó gyökerében a kibontott, szerkeszthető forrás található. Az eredetileg átadott ZIP és APK változatlanul megmaradt.

Teszteléshez Node.js, Python 3 és JDK 17+ szükséges:

```bash
npm ci
npx playwright install --with-deps chromium
npm test
python3 scripts/verify_release.py
```

A GitHub Actions minden feltöltésnél és pull requestnél futtatja a teszteket; `v*` tag esetén ellenőrzött kiadási mellékletekkel GitHub Release-t készít. Az automatizálás a már átadott APK-t teszi közzé, nem írja alá újra.

- [CONTRIBUTING.md](CONTRIBUTING.md): közreműködés és hibajelentés.
- [docs/RELEASE.md](docs/RELEASE.md): kiadási folyamat és a külön letöltőoldal közzététele.
- [docs/ADATKEZELES.md](docs/ADATKEZELES.md): helyi tárolás, titkosítás és mentések.

- [PROJECT_HANDOFF.md](PROJECT_HANDOFF.md): projektcél, döntések és a Codex általi átvétel.
- [AGENTS.md](AGENTS.md): adatvédelmi, kompatibilitási és fejlesztési szabályok.
- [BUILDING.md](BUILDING.md): APK-build és megismételhető tesztek.
- [VALIDATION.md](VALIDATION.md): eredmények és vizsgálati korlátok.
- [CHANGELOG.md](CHANGELOG.md): változásnapló.

A GitHubra előkészített forráscsomag **nem tartalmaz aláírókulcsot vagy személyes naplót**.
A kulcs külön privát ZIP-ben van; sem azt, sem a jelszavát ne töltsd a repositoryba.

Az alkalmazás helyi HTML/CSS/JavaScript + Java WebView. Nincs internetes szolgáltatás,
fiók, reklám, analitika, külső betűtípus, fotó-, hang- vagy felhőszinkron.
Minden grafika saját, szerkeszthető SVG a `memory-art.js` modulban; nincs stockkép vagy
külső grafikai függőség. Az eredeti launcherikonok is saját rajzok.
A saját kód nyílt forrású licencéről a tulajdonos még nem döntött.
A forrás elérhetősége önmagában nem ad általános továbbfelhasználási vagy terjesztési engedélyt.
