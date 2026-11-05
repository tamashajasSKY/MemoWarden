# GitHub-kiadás és letöltőoldal

A README és a `docs/index.html` a [v1.1.0 GitHub Release](https://github.com/tamashajasSKY/MemoWarden/releases/tag/v1.1.0) eredeti APK-mellékletére mutat. A letöltéshez nem kell újrafordítani az alkalmazást. A forráscsomagot és az APK-t a repóban is változatlanul őrizzük; ellenőrzésük:

```bash
sha256sum -c SHA256SUMS
python3 scripts/verify_release.py
```

## Verziózott GitHub Release

A `.github/workflows/release.yml` egy `v*` tag feltöltésére fut. Előbb lefuttatja a teljes tesztcsomagot és a kiadási fájlok ellenőrzését, majd közzéteszi az APK-t, az eredeti forrás ZIP-et és az ellenőrzőösszegeket egy GitHub Release-ben. A munkafolyamat GitHub Actions által biztosított, a repóra korlátozott tokent használ. Saját token vagy aláírókulcs nem szükséges; az APK-t nem fordítja és nem írja alá újra.

Az 1.1.0-hoz a `v1.1.0` tag és a `docs/releases/v1.1.0.md` tartozik. Új kiadáskor a verziókat, a kiadási fájlokat, az `apk-validation.json` fájlt, az ellenőrzőösszegeket, a dokumentációt és a kiadási jegyzetet együtt frissítsd, majd csak sikeres ellenőrzés után küldd fel a megfelelő taget. Már közzétett kiadási fájlt ne írj felül csendben.

Ha a GitHub Actions szervezeti vagy repóbeállítás miatt tiltott, a kiadás nem készül el automatikusan. Az Actions lapon ellenőrizd az eredményt. Az APK a README közvetlen linkjéről ettől függetlenül letölthető.

## Külön GitHub Pages-weboldal

A `docs/index.html` egy önálló, mobilon is használható bemutató- és letöltőoldal, külső függőségek nélkül. Közzétételéhez a GitHub repó **Settings → Pages** részében válaszd a **Deploy from a branch**, **main**, **/docs** beállítást, majd mentsd.

Az oldal várható címe `https://tamashajasSKY.github.io/MemoWarden/`; csak sikeres Pages-telepítés után tekinthető élőnek. Privát repónál a GitHub-előfizetés és a hozzáférési beállítások is számítanak. A GitHub repó README-je már külön Pages-beállítás nélkül megjeleníti a letöltési linket.
