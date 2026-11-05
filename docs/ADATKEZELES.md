# Adatkezelés

Ez a leírás az Emlékőr 1.1.0 forrásában megvalósított működést ismerteti; nem független biztonsági tanúsítás.

## Android

- A napló az alkalmazás privát tárában marad. A natív tárolás Android Keystore-kulccsal és AES-256-GCM titkosítással működik.
- A WebView DOM Storage használata tiltott; az adattárat a Java bridge kezeli.
- A manifest nem kér Android-engedélyt, internetes engedélyt sem. Nincs felhasználói fiók, analitika, reklám vagy felhőszinkron.
- A megosztás és a fájlexport a felhasználó műveletére, az Android rendszerfelületén indul. Az így megosztott tartalom további kezelését a választott célalkalmazás végzi.
- Az alkalmazás eltávolítása vagy a telefon elvesztése a helyi adatok elvesztésével járhat. Készíts külön jelszavas mentést.

## Hordozható mentés

A `.emlekor` fájl `EMLEKOR1` formátumot használ: PBKDF2-HMAC-SHA256, 210 000 iteráció, véletlen só, AES-256-GCM titkosítás. A jelszó nincs eltárolva és nem állítható helyre. A mentésfájlt és a jelszót biztonságos, külön helyen őrizd.

A visszatöltés előnézetet és megerősítést kér; a helyi emlékeket megtartja, az azonosakat nem duplázza, az eltérő változatokat külön bejegyzésként őrzi meg.

## Böngészős fejlesztői előnézet

A böngészős változat localStorage-ot használ, titkosítás nélkül. Ez eltér az Android-alkalmazás natív tárolásától. Az előnézetbe és a tesztekbe kizárólag kitalált tesztadatokat írj. A jelszavas export ebben a környezetben is titkosított.

## GitHub és letöltőoldal

A dokumentációs letöltőoldal nem naplóalkalmazás: nem kér emléket vagy személyes adatot, és nem tartalmaz saját analitikát. A repó, a letöltések és egy esetleges GitHub Pages-oldal kiszolgálását a GitHub végzi, a saját adatkezelési feltételei szerint.

Személyes naplót, mentést, jelszót vagy aláírókulcsot hibajegyhez se csatolj. [Ellenőrzések és korlátok](../VALIDATION.md).
