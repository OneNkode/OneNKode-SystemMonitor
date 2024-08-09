# System-monitor-NDXworks



## Áttekintés

Az **NDXworks** egy Python alapú rendszermonitorozó eszköz, amely valós időben figyeli a CPU és memória használatot, valamint megjeleníti a rendszerinformációkat, például a teljes RAM mennyiségét és a GPU-k nevét és memória kapacitását. Az alkalmazás az egyszerűség és az esztétikai megjelenés érdekében színekkel jelzi a használati adatokat, és egyéni ikonnal rendelkezik az elkészített EXE fájlhoz.

## Funkciók

- Valós idejű CPU és memória használat monitorozás
- Rendszerinformációk megjelenítése (operációs rendszer, CPU, memória, GPU)
- Színes megjelenítés a használati adatokhoz
- Egyéni ikon az EXE fájlhoz

## Telepítés

### Szükséges könyvtárak

A program futtatásához szükséges Python könyvtárak:
- `psutil`: A rendszer erőforrásainak monitorozásához
- `colorama`: Színes szöveg megjelenítéséhez a terminálban
- `GPUtil`: GPU információk lekérdezéséhez

Telepítheted ezeket a könyvtárakat a következő parancsokkal:

```bash
pip install psutil colorama GPUtil
