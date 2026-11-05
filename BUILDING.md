# Emlékőr – build és teszt

## Android APK

Python 3, JDK 17, Android SDK Platform 35 és Build Tools 35.0.0 szükséges.
A build nem igényel Gradle-t vagy hálózatot, ha az eszközök már telepítve vannak.

1. A külön privát mentésből helyezd vissza az eredeti `signing/emlekor.jks` kulcsot,
   vagy add meg az útvonalát az `EMLEKOR_KEYSTORE` környezeti változóban.
2. Állítsd be az SDK helyét és a kulcs jelszavát; utóbbit ne írd forrásfájlba.

   ```bash
   export ANDROID_HOME=/absolute/path/to/android-sdk
   read -rsp 'Keystore password: ' EMLEKOR_KEY_PASSWORD
   export EMLEKOR_KEY_PASSWORD
   python3 build.py
   unset EMLEKOR_KEY_PASSWORD
   ```

3. Kimenet: `dist/Emlekor-1.1.0.apk`. A build az aláírást és a ZIP sértetlenségét ellenőrzi,
   majd atomi átnevezéssel teszi elérhetővé a csomagot.
4. Javac hiányában `ECJ_JAR=/absolute/path/to/ecj.jar` használható. Az aktuális kiadás
   ECJ-vel fordult, Linuxon. Windows alatt a szkript futtatásához WSL ajánlott.
5. Hiányzó eredeti kulcsnál vagy jelszónál a build leáll. Csak külön tesztidentitáshoz
   engedélyezhető új kulcs az `ALLOW_NEW_SIGNING_KEY=1` kapcsolóval. Eltérő aláírású APK
   a meglévő telepítésre nem frissíthető.

Régi és új tanúsítvány összevetése:

```bash
"$ANDROID_HOME/build-tools/35.0.0/apksigner" verify --print-certs OLD.apk
"$ANDROID_HOME/build-tools/35.0.0/apksigner" verify --print-certs dist/Emlekor-1.1.0.apk
```

A SHA-256 tanúsítványlenyomatnak egyeznie kell. Csomagnév `hu.emlekor.naplo`,
aktuális versionCode 2, versionName 1.1.0. A minimum API 26, cél-API 35.

## Böngészős fejlesztés

Nyisd meg az `app/src/main/assets/index.html` fájlt. A böngészős előnézet localStorage-ot
használ, és a helyi adatok ott nem titkosítottak. Androidon DOM Storage tiltva van;
a Java bridge kezeli a titkosított adattárat. A jelszavas export mindkét környezetben titkosított.

## Automatikus tesztek

```bash
npm ci
npx playwright install chromium
npm test
```

A `package.json` a kipróbált Playwright-verziót rögzíti. Saját Chromiumhoz add meg a
`CHROME_PATH` abszolút útvonalat. Javac nélküli környezetben az `ECJ_JAR` is szükséges:

```bash
CHROME_PATH=/path/to/chrome ECJ_JAR=/path/to/ecj.jar python3 run_tests.py
```

A futtató először lefordítja a Java CryptoCli segédet és a CryptoBoxot, majd futtatja:

- `tests/test-app.cjs`: írás, szerkesztés, mentés, Java/WebCrypto kompatibilitás, hibaágak.
- `tests/test-offline.cjs`: helyi fájlból, tesztfelület nélkül működő app és export.
- `tests/test-growth.cjs`: ösvények, albumok, jelvények, kertválasztás, 1.0-s migráció,
  napi jutalomkorlát, nagy betűk és négy kijelzőméret.

A tesztek megbízható helyi projektkóddal, izolált fejlesztői környezetben futtathatók;
Chromium `--no-sandbox` kapcsolót használnak. A képek és szintetikus tesztmentések `qa/`
alá kerülnek, és nem részei a forráscsomagnak. Valódi naplót ne használj a tesztekben.

## Kiadás

1. Növeld a manifest verziókódját és verziónevét; frissítsd a build és csomagoló verzióját,
   a package.json, README, a HTML kiadásjelzése és CHANGELOG.md adatait.
2. Tesztek, APK-build, majd `ANDROID_HOME=... PREVIOUS_APK=/path/to/old.apk python3 package_release.py`.
3. A csomagoló ellenőrzi az assetegyezést, aláírást, a hálózati engedély hiányát,
   a régi tanúsítványt (ha megadtad), és elkészíti az APK-t és a kulcsmentes forrás ZIP-et.
4. A privát kulcsmentést külön őrizd. Ne tedd gitbe vagy GitHub Release mellékletébe.

Nincs Gradle/Android Studio projekt, wrapper vagy Play Store-kiadási folyamat.
Ezek hozzáadása külön fejlesztés. Bolti beküldés előtt az akkori API-, adatvédelmi,
aláírási és publikálási követelményeket külön ellenőrizni kell.
