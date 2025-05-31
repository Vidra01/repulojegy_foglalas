from abc import ABC, abstractmethod

# --- Járat absztrakt osztály ---
class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_tipus(self):
        pass

# --- Belföldi Járat ---
class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def jarat_tipus(self):
        return "Belföldi"

# --- Nemzetközi Járat ---
class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)

    def jarat_tipus(self):
        return "Nemzetközi"

# --- JegyFoglalás ---
class JegyFoglalas:
    def __init__(self, jarat, utas_nev):
        self.jarat = jarat
        self.utas_nev = utas_nev

    def __str__(self):
        return f"{self.utas_nev} - {self.jarat.jaratszam} ({self.jarat.jarat_tipus()})"

# --- LégiTársaság ---
class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []
        self.foglalasok = []

    def jarat_hozzaadas(self, jarat):
        self.jaratok.append(jarat)

    def foglalas_letrehozas(self, jaratszam, utas_nev):
        jarat = next((j for j in self.jaratok if j.jaratszam == jaratszam), None)
        if not jarat:
            return f"Nincs ilyen járat: {jaratszam}"
        foglalas = JegyFoglalas(jarat, utas_nev)
        self.foglalasok.append(foglalas)
        return f"Foglalás sikeres: {foglalas}, Ár: {jarat.jegyar} Ft"

    def foglalas_lemondas(self, utas_nev, jaratszam):
        for f in self.foglalasok:
            if f.utas_nev == utas_nev and f.jarat.jaratszam == jaratszam:
                self.foglalasok.remove(f)
                return f"Foglalás lemondva: {f}"
        return "Nem található ilyen foglalás."

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            return "Nincs jelenleg foglalás."
        return "\n".join(str(f) for f in self.foglalasok)

# --- Tesztadatok betöltése ---
def rendszer_inditasa():
    lt = LegiTarsasag("Példa Airlines")
    lt.jarat_hozzaadas(BelfoldiJarat("B101", "Budapest", 15000))
    lt.jarat_hozzaadas(BelfoldiJarat("B102", "Debrecen", 12000))
    lt.jarat_hozzaadas(NemzetkoziJarat("N201", "London", 55000))
    lt.foglalas_letrehozas("B101", "Kovács Anna")
    lt.foglalas_letrehozas("B102", "Nagy Péter")
    lt.foglalas_letrehozas("N201", "Tóth Márk")
    lt.foglalas_letrehozas("B101", "Szabó Lili")
    lt.foglalas_letrehozas("N201", "Horváth Dániel")
    lt.foglalas_letrehozas("B102", "Kiss Gergő")
    return lt

# --- Főmenü ---
def main():
    lt = rendszer_inditasa()

    while True:
        print("\n--- Repülőjegy Foglalási Rendszer ---")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Válassz egy lehetőséget: ")

        if valasztas == "1":
            nev = input("Add meg az utas nevét: ")
            jaratszam = input("Add meg a járatszámot: ")
            print(lt.foglalas_letrehozas(jaratszam, nev))
        elif valasztas == "2":
            nev = input("Add meg az utas nevét: ")
            jaratszam = input("Add meg a járatszámot: ")
            print(lt.foglalas_lemondas(nev, jaratszam))
        elif valasztas == "3":
            print("\nAktuális foglalások:")
            print(lt.foglalasok_listazasa())
        elif valasztas == "4":
            print("Kilépés a rendszerből...")
            break
        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()
