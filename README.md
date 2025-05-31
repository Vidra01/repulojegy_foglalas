# repulojegy_foglalas
# Repülőjegy Foglalási Rendszer – Python
Ez a program egy egyszerű, Python nyelvű szöveges felületen működő repülőjegy-foglaló rendszer.
A célja az volt, hogy objektumorientált megközelítéssel modellezzünk egy légitársaság járat- és foglaláskezelési működését.
## Fő funkciók
* Két járattípus kezelésének lehetősége: belföldi és nemzetközi járatok
* Járatok nyilvántartása egy adott légitársaságon belül
* Jegyfoglalás, foglalás törlése és a meglévő foglalások megjelenítése
* Egyszerű, parancssoros kezelőfelület
* A rendszer előre feltöltve indul néhány minta járattal és foglalással a kipróbálás megkönnyítésére
## Működési felépítés
A rendszer a következő osztályokra épül:
* `Jarat` – egy absztrakt alaposztály, amely meghatározza a közös járatjellemzőket
* `BelfoldiJarat` és `NemzetkoziJarat` – a konkrét járattípusokat leíró osztályok
* `LegiTarsasag` – a járatok és az utasfoglalások kezelését végzi
* `JegyFoglalas` – egy konkrét utas adott járatra szóló foglalását tárolja
A program indításakor egy előre beállított járat- és foglaláslista kerül betöltésre, és ezután a felhasználó a konzolon keresztül hajthatja végre a kívánt műveleteket.
