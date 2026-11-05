# Emlékőr 1.1.0 – ellenőrzés

## GitHub-repó előkészítése – 2026. november 5.

Az eredeti APK és forrás ZIP változatlanul került a repóba. A `scripts/verify_release.py`
ellenőrizte mindkét fájl SHA-256 összegét, a ZIP-ek sértetlenségét és az APK mind az öt
webes assetjének bájtra egyezését a kibontott forrással. Ez az ellenőrzés nem helyettesíti
az APK-aláírás SDK-eszközzel végzett vizsgálatát.

Ebben a felhőkörnyezetben a `tests/test-app.cjs` **63 ellenőrzése sikeres** volt,
Java/WebCrypto együttműködéssel, külső kérések és JavaScript-hibák nélkül.
A `test-offline.cjs` első oldalbetöltése `ERR_BLOCKED_BY_ADMINISTRATOR` hibával leállt,
mert a telepített Chromium szabályzata tiltja a `file://` megnyitását. Az offline csoport
8 ellenőrzése nem fejeződött be, a futtató pedig ezután nem indította el a növekedési
csoport 41 ellenőrzését. A szabályzatot nem módosítottuk. A teljes csomaghoz külön
GitHub Actions munkafolyamat készült; annak eredménye az Actions lapon ellenőrizhető.

## Az eredeti forráscsomaghoz mellékelt vizsgálati jelentés

Az alábbi eredmények a feltöltött csomag korábbi jelentéséből származnak.
Nem a mostani felhőkörnyezetben végzett új aláírás- vagy telefonos vizsgálat eredményei.

2026. november 5. **112 sikeres automatizált ellenőrzés.**

| Csoport | Ellenőrzés |
|---|---:|
| Napló, adattár, Java/WebCrypto és hibaágak | 63 |
| Offline, éles felület és jelszavas fájlexport | 8 |
| Új grafika, kert, ösvények, albumok és migráció | 41 |

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

V2/v3 aláírás érvényes, ZIP sértetlen, az összes (5) beágyazott webes asset
bájtra egyezik a forrással. Csomag hu.emlekor.naplo, verzió 1.1.0 / 2,
minSdk 26, targetSdk 35. Nincs kért Android-engedély, hálózati engedély sem.
A tanúsítvány egyezik az 1.0.0 APK-val.
Méret: 54369 bájt. SHA-256: `e71de1b76217dd9937ed3db40ac6f3a9ad79e55e92840f6babb354dd13e40a99`.

A forráscsomagban nincs signing mappa, jelszó, személyes napló, mentésfájl,
QA-kép vagy buildkönyvtár. A kulcs külön privát ZIP-ben marad.
A natív adattárolási és kriptográfiai Java-fájlok változatlanok az 1.0-s kiadáshoz képest.

## A vizsgálat határa

**Fizikai Android-telefonos teszt nem történt.** A Keystore, AtomicFile,
rendszermegosztás, dokumentumválasztó, képernyőbillentyűzet és akadálymentes
felolvasás működését konkrét telefonon is ellenőrizni kell. A böngészős bridge-szimuláció
nem helyettesíti a natív integrációs próbát; Androidos biztonsági minősítés nem történt.
