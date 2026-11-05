# Emlékőr – fejlesztési szabályok

- Előbb olvasd el a PROJECT_HANDOFF.md és BUILDING.md fájlokat.
- Önálló alkalmazás: `hu.emlekor.naplo`. A RiftBramble játéktól külön kulcs és adattár.
- A napló személyes adat. Külső küldést, analitikát, fiókot vagy felhőt csak külön kérésre adj hozzá.
- Androidon a helyi adatokat kizárólag a titkosított natív tárral kezeld. DOM Storage ott tiltott.
- A szövegsegéd csak a megadott részleteket rendezheti; hiányzó emléket vagy érzést nem találhat ki.
- Az import a helyi emlékeket ne írja felül. Az eltérő változatokat is őrizd meg, azonosat ne duplázz.
- Az olvashatatlan natív tárat ne írd felül üres adattal. Mentési hibánál őrizd meg a szerkesztett szöveget.
- Az aláírókulcs és a jelszó privát, nincs a forráscsomagban. Személyes napló, mentésfájl és QA sem kerülhet gitbe.
- Az eredeti kulcs hiányában ne generálj csendben másik aláírást és ne állíts frissíthetőséget.
- Őrizd meg a csomagnevet, az aláírást és a mentéskompatibilitást. Kiadásonként növeld a verziókódot.
- A haladás a mentett emlékekből számolódik. Napi 10 levél, nincs streakvesztés, határidő, ranglista vagy büntetés.
- A nehéz és vegyes hangulatú emlékek ugyanúgy számítanak. Ösvény bármikor kihagyható.
- A dekoratív SVG-be soha ne interpolálj felhasználói szöveget. Azt textContenttel jelenítsd meg.
- A saját SVG-grafikai stílust, nagy betűs módot és legalább 44 px-es fő érintőfelületeket őrizd meg.
- Ellenőrizd a mentést, visszatöltést, régi formátumot, hibaágakat, reszponzivitást és az offline használatot.
- Fizikai telefonos tesztet csak tényleges eszközpróba után állíts.
