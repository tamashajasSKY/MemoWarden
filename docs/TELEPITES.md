# Telepítés és frissítés

Az Emlékőr 1.1.0 Android 8.0-tól használható. Csomagnév: `hu.emlekor.naplo`.

## Első telepítés

1. Nyisd meg a [hivatalos repót](https://github.com/tamashajasSKY/MemoWarden) a telefonodon.
2. Kattints az [APK letöltése](https://github.com/tamashajasSKY/MemoWarden/raw/refs/heads/main/Emlekor-1.1.0.apk) linkre.
3. A Letöltések közül nyisd meg az `Emlekor-1.1.0.apk` fájlt.
4. Ha a telefon kéri, a használt böngésző vagy fájlkezelő beállításában engedélyezd az ismeretlen alkalmazások telepítését. A menüpont neve gyártónként eltérhet.
5. Telepítsd az alkalmazást, majd indítsd el. A telepítési engedélyt utána visszavonhatod.

## Meglévő napló frissítése

Előbb az alkalmazás **Beállítások → Jelszavas biztonsági másolat** menüjében mentsd ki a naplót, és őrizd meg a fájlt és a jelszavát.

A régi alkalmazást hagyd telepítve, és nyisd meg az új APK-t. Android csak azonos csomagnév és megfelelő aláírás esetén enged frissítést. Ha ütközést vagy aláírási hibát jelez, ne töröld az alkalmazást: ellenőrizd a kiadást és kérj segítséget. Eltávolításkor a helyi napló és az ahhoz tartozó kulcs elveszhet.

## Átköltözés másik telefonra

Telepítsd az Emlékőrt az új telefonon. A Beállításokban válaszd a **Mentés visszatöltése** lehetőséget, add meg a `.emlekor` fájlt és a hozzá tartozó jelszót, majd az előnézet után erősítsd meg a visszatöltést. A jelszóhoz nincs helyreállítási szolgáltatás.

## Ha a letöltés vagy telepítés nem sikerül

- Ellenőrizd, hogy valóban `.apk` fájlt töltöttél le, nem a forráskód ZIP-jét.
- Az APK mérete 54 369 bájt; az ellenőrzőösszeg a repó `SHA256SUMS` fájljában szerepel.
- Android 8.0-nál régebbi rendszerre ez a verzió nem telepíthető.
- Meglévő telepítésnél előbb készíts mentést; aláírási hiba miatt ne távolítsd el automatikusan.

Fizikai telefonos telepítési és frissítési teszt még nem történt. [Az ellenőrzések határa](../VALIDATION.md).
