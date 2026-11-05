# Emlékőr – projektátadás Codexnek

> Eredeti átadási dokumentum a feltöltött 1.1.0-s csomagból. A forrás azóta a
> `tamashajasSKY/MemoWarden` repó gyökerébe került; a lentebb szereplő, még hátralévő
> feltöltésre vonatkozó megjegyzések az átadáskori állapotot írják le.

Állapot: **1.1.0**, 2026. november 5. Tulajdonos: Tamás Hajas (Kardhal).
Projektkörnyezet: „Android appok”. Ez a RiftBramble-től teljesen különálló alkalmazás.
Az eredeti kérés: „Értéket teremtünk, emlékeket védünk.” Napi pár perces, vezetett,
kulcsszavakkal segített napló gyerektől idősig, Androidra telepíthető APK-val.

A fogadó Codex nem látja automatikusan a ChatGPT Work-projektet. A ZIP önmagában
átadja a teljes szükséges forrást, a döntéseket és a megismételhető buildet.

## A fogadó Codex feladata

Olvasd el ezt a fájlt, az AGENTS.md-t és a BUILDING.md-t. A ZIP `Emlekor-1.1.0/`
mappájának **kibontott tartalmát** tedd a felhasználó által kiválasztott Emlékőr
GitHub-repository gyökerébe. Ne az archívumot commitold egyetlen bináris fájlként.
Őrizd meg a repositoryban már meglévő, nem kapcsolódó munkát. A konkrét GitHub URL
itt nincs megadva; ne téveszd össze a `riftbramble` repositoryval. Ha nincs kijelölt
célrepository, azt a feltöltés előtt tisztázni kell a felhasználóval.

Futtasd a teszteket, nézd át a változásokat, és kövesd a repository engedélyezett
branch/PR munkafolyamatát. A jelen csomag nem jelenti, hogy GitHub-feltöltés történt.
Kiadásonként kész APK-t, forrást és rövid magyar változásleírást adj át.

## Folytonosság és érzékeny adatok

- Csomagnév `hu.emlekor.naplo`; Android 8.0+, minSdk 26, targetSdk 35.
- Aktuális verziókód 2, verziónév 1.1.0. Eredeti aláírókulcs külön privát ZIP-ben.
- A kulcs és jelszava, valamint személyes napló és `.emlekor` mentés nem kerülhet gitbe.
- Meglévő emléket, felhasználói megfogalmazást vagy piszkozatot ne írj át migrációkor.
- Az alapkiadás offline; nincs INTERNET engedély, fiók, reklám, telemetria vagy külső AI.
- Fizikai telefonos próba még nem történt. Böngészős tesztet ne írj le telefonosként.

## Eredeti funkciók, amelyeknek meg kell maradniuk

Háromlépéses írás: pillanat → kapaszkodók → szerkeszthető történet. Cím, dátum,
opcionális hangulat/emberek/hely, kulcsszavak, történés, részlet és személyes jelentés.
Az offline szövegrendezés csak a megadott szavakat és részleteket kapcsolja össze.
Nem találhat ki eseményt vagy érzést. Puszta kulcsszóból is menthető emlék.

Automatikus piszkozatmentés és folytatás; három kérdésstílus (Rövid és játékos,
Mindennapi pillanatok, Élettörténet); nagyobb betűk; keresés ékezet- és kisbetűfüggetlenül;
kedvencek, újraolvasás, szerkesztés, egyenkénti törlés és megerősített teljes törlés.
A megosztás csak a felhasználó külön gombnyomására indulhat a rendszeren keresztül.

## 1.1-es grafika és gamifikáció

A saját, szerkeszthető SVG-stílus folytatódik. Emlékkönyv, képes naplókártyák,
hangulatjelek, szerkesztési lépésképek, jelvények és részletes kert készült.
A kertben pad, tó, virágok; később házikó, pillangó és új fák jelennek meg.
Hat növekedési szint: 0, 1, 5, 15, 30 és 100 emléktől.

| Elem | Működés |
|---|---|
| Nyolc emlékösvény | Kapcsolatok, érzékek, gyökerek, hétköznapok, felfedezés, ami megtartott, természet, továbbadott szavak |
| Ösvényhaladás | Három megőrzött emlék az adott ösvény eltávolítható jelölő kulcsszavával |
| Hat album | Kulcsszavas csoportosítás; emberek albumba a megadott emberek mező is beleszámít |
| Tizenkét jelvény | Emlékszám, külön írásnapok, részletek, kedvencek, régi napok, emberek és bejárt ösvények |
| Emléklevelek | Naponta egyszer 10, a meglévő emlékek recordedDay mezőjéből számolva |
| Négy kert | Tavasz alapból, alkony 30, csillagliget 70, ősz 150 levéltől |
| Visszajelzés | Új mentéskor képes visszajelzés; új levél csak új írásnapra |

Nincs elkölthető pénz, verseny, határidő, elvesző streak vagy büntetés.
A nehéz emlékek ugyanúgy számítanak. Az ösvényeket nem kell teljesíteni.
A haladás az aktuális emlékekből származik, ezért törléskor újraszámolódik.
A kiválasztott kert opcionális `settings.theme` beállítás; ha a szükséges emlékek törlődnek,
a megjelenítés visszavált az alapra, az emlékszöveghez nem nyúl.

A témák és az albumok nem AI-tartalomelemzés eredményei: a jelölő szavak és a megadott
mezők alapján működnek. A meglévő piszkozatot az ösvényválasztás nem címkézi át.
Minden SVG saját forráskód; felhasználói szöveg nem kerül SVG/HTML-interpolációba.

## Adattár és titkosítás

A JSON formátuma továbbra is `app: emlekor`, `version: 1`. Régi 1.0-s mentésnél
az opcionális téma hiánya az alap tisztást jelenti. A régi bejegyzések megmaradnak.

Android: DOM Storage tiltva, Java bridge → privát `AtomicFile` → Android Keystore
AES-256-GCM. Olvasási hibánál az app nem ír üres naplót a sérült tárra.
Böngészős előnézet: `emlekor.data.v1` localStorage kulcs, helyben titkosítatlan.
Ezt az app a Beállításokban jelzi; ne keverd össze az Android védett tárolásával.

Hordozható `.emlekor`: EMLEKOR1 formátum, PBKDF2-HMAC-SHA256, 210000 iteráció,
16 bájt véletlen só, AES-256-GCM, 12 bájt IV, 128 bites tag.
A lokális és hordozható titkosítás külön kontextuscímkét használ.
A jelszó nincs eltárolva és nem helyreállítható. Külön mentés nélkül az alkalmazás
eltávolítása vagy a telefon elvesztése adatvesztéshez vezethet.

Import: előnézet és megerősítés; helyi bejegyzések megtartása, azonosak deduplikálása,
eltérő változatok megőrzése új ID-val és restoredFrom hivatkozással. A helyi piszkozat
és olvasási beállítás normál importkor elsőbbséget élvez. Nincs jutalomegyenleg-összeadás.

## Kódtérkép

| Fájl | Felelősség |
|---|---|
| `app/src/main/assets/index.html` | Oldalak, űrlapok, navigáció és párbeszédablakok |
| `style.css` ugyanott | Reszponzív, nagy betűs felület és csökkentett mozgás |
| `app.js` | Naplóállapot, validálás, CRUD, piszkozat, export/import és UI |
| `journeys.js` | Ösvények, albumok, jelvények, kertfeloldás; tiszta, származtatott számítások |
| `memory-art.js` | Saját, dinamikus SVG-illusztrációk |
| `MainActivity.java` | WebView, életciklus, helyi kérések és Android vissza gomb |
| `MemoryBridge.java` | Natív adattár, dokumentumválasztó és rendszermegosztás |
| `CryptoBox.java` | Tiszta Java kriptográfia, böngészővel kompatibilis mentés |
| `build.py` | SDK/JDK-alapú, eredeti kulccsal aláírt APK |
| `run_tests.py`, `tests/` | Java/WebCrypto és böngészős ellenőrzések |
| `package_release.py` | Ellenőrzött APK és kulcsmentes átadási ZIP |

Nincs bundler, frontend keretrendszer, Gradle wrapper vagy webszerver-függőség.
A script-sorrend: memory-art.js → journeys.js → app.js. A tesztfelület csak `?test=1`
mellett létezik; éles megnyitáskor nincs `EmlekorTest`.

## Korlátok és következő lehetséges feladatok

- Valódi telefonon telepítés/frissítés, Keystore, dokumentumválasztó, rendszermegosztás,
  képernyőbillentyűzet és akadálymentes felolvasás próbája szükséges.
- Hosszabb, valódi naplókkal végzett használhatósági próba hátravan; ne adj személyes naplót teszthez.
- Nincs fénykép, hangfelvétel, felhőfiók, automatikus értesítés vagy internetes AI.
  Ezek új adatvédelmi és mentési döntéseket igényelnének, külön kérés nélkül ne építsd be őket.
- Nincs kijelölt végleges nyílt forráskódú licenc vagy Play Store-publikálási folyamat.
- A jelen feladat nem kéri új repository létrehozását és nem végzett GitHub-feltöltést.

A pontos teszteredmények és a natív vizsgálat határa a VALIDATION.md-ben található.
