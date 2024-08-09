# NDXworks - Rendszerfigyelő Alkalmazás
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

first install : install_dependencies.py

**NDXworks** egy egyszerű, de hatékony parancssori rendszerfigyelő alkalmazás, amely valós időben megjeleníti a rendszer erőforrásainak állapotát és statisztikáit. A programot Python nyelven írtuk, és a PyInstaller segítségével készült egy önálló végrehajtható fájl (.exe), amely Windows rendszeren futtatható.

## Funkciók

### 1. CPU Használat Monitorozása
- Az alkalmazás valós időben nyomon követi a CPU használatát és színesen jeleníti meg a százalékos értéket:
  - **Zöld**: 0% - 49%
  - **Sárga**: 50% - 74%
  - **Piros**: 75% - 100%

### 2. Memória Használat Monitorozása
- Valós időben megjeleníti a memória használatát, szintén színesen:
  - **Zöld**: 0% - 49%
  - **Sárga**: 50% - 74%
  - **Piros**: 75% - 100%

### 3. GPU Információk
- Az alkalmazás lekérdezi és megjeleníti a telepített GPU(k) nevét és memóriáját. Ha nincs elérhető GPU, az alkalmazás jelzi ezt is.

### 4. Lemezhasználat Monitorozása
- Megjeleníti a lemezhasználatot százalékos formában és az összes elérhető lemezkapacitást.

### 5. Hálózati Használat Monitorozása
- Az alkalmazás megjeleníti az összesített be- és kimenő hálózati forgalmat MB-ban.

### 6. Rendszerinformációk
- A rendszerinformációkat tartalmazó szakasz megjeleníti a következőket:
  - **Operációs rendszer**: Windows verzió és kiadás
  - **CPU**: CPU típusa és magok száma
  - **Teljes RAM**: Rendszer memóriája GB-ban

### 7. Ikon és Verzió
- Az alkalmazás ikont tartalmaz, amely az `assets/icon.ico` fájlban található.
- A verziószám a kijelző tetején található (`V1.3`).

## Telepítés és Használat

1. **Python Telepítése**: 
   - Bizonyosodj meg róla, hogy a Python 3.x telepítve van a rendszereden.

2. **Szükséges Könyvtárak Telepítése**:
   - Telepítsd a szükséges Python csomagokat a következő parancsok futtatásával:
     ```bash
     pip install psutil gputil colorama
     ```

3. **A Program Futtatása**:
   - A program futtatásához egyszerűen indítsd el a létrehozott végrehajtható fájlt (`index.exe`), amelyet a PyInstaller készít.
   - A program futtatása után a rendszerfigyelő információk valós időben frissülnek a parancssori felületen.

4. **Forráskód és Hozzájárulás**:
   - A teljes forráskód elérhető a GitHub oldalon. Ha szeretnél hozzájárulni a projekt fejlődéséhez vagy bugokat jelenteni, kérlek, nyiss egy [issue-t](https://github.com/username/ndxworks/issues) vagy egy [pull requestet](https://github.com/username/ndxworks/pulls).

## Képernyőképek

Az alábbiakban láthatók a program képernyőképei, amelyek bemutatják, hogyan néz ki a felhasználói felület és a rendszerinformációk:

![Screenshot](assets/screenshot.png)

## Közreműködés

Kérjük, olvasd el a [Hozzájárulási irányelvek](CONTRIBUTING.md) dokumentumot, ha szeretnél hozzájárulni a projekthez.

## Licenc

Ez a projekt az MIT Licenc alatt áll. További információkért lásd a [LICENSE](LICENSE) fájlt.

---

Kérlek, ha bármilyen kérdésed van a program működésével vagy telepítésével kapcsolatban, ne habozz megkérdezni!


### Szükséges könyvtárak

A program futtatásához szükséges Python könyvtárak:
- `psutil`: A rendszer erőforrásainak monitorozásához
- `colorama`: Színes szöveg megjelenítéséhez a terminálban
- `GPUtil`: GPU információk lekérdezéséhez

Telepítheted ezeket a könyvtárakat a következő parancsokkal:

```bash
pip install psutil colorama GPUtil
