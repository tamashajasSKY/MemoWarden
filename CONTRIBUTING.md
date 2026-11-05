# Közreműködés

Fejlesztés előtt olvasd el az [AGENTS.md](AGENTS.md), [PROJECT_HANDOFF.md](PROJECT_HANDOFF.md) és [BUILDING.md](BUILDING.md) fájlokat. A licenc még nincs kiválasztva; továbbfelhasználás előtt egyeztess a tulajdonossal.

## Hiba bejelentése

GitHub Issue-ban add meg az alkalmazás verzióját, az Android verzióját, a készülék típusát, a megismétlés lépéseit, valamint a várt és a tényleges működést. Csak kitalált adatokkal készült képet vagy példát használj. Személyes naplót, `.emlekor` mentést, jelszót és kulcsot ne csatolj.

## Változtatás ellenőrzése

```bash
npm ci
npx playwright install --with-deps chromium
npm test
python3 scripts/verify_release.py
```

A tesztek Python 3-at és JDK 17+-t is igényelnek; alternatív Java-fordító és böngésző beállítása a BUILDING.md fájlban található. Az automatikus ellenőrzések nem helyettesítik a valódi Android-eszközön végzett próbát.

Őrizd meg a csomagnevet, a mentéskompatibilitást és a veszteségkerülő importot. Új kiadáshoz az eredeti aláírókulcs szükséges; azt soha ne commitold. A változtatásokat rövid leírással és a tényleges ellenőrzési eredményekkel add be.
