from shop import proizvodi
from shop import narudzbe

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

for proizvod in proizvodi_za_dodavanje:
    novi_proizvod = proizvodi.Proizvod(
        proizvod["naziv"],
        proizvod["cijena"],
        proizvod["dostupna_kolicina"]
    )
    proizvodi.dodaj_proizvod(novi_proizvod)

for proizvod in proizvodi.skladiste:
    proizvod.ispis()

narudzbe.napravi_narudzbu(proizvodi_za_dodavanje)


# nisam siguran da li je zadatak krivo postavljen ili je trik pitanje, ali kako bi ovo radilo potrebno je promijeniti ključ 'dostupna_kolicina' u 'narucena_kolicina'

proizvodi_za_dodavanje_x = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "narucena_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "narucena_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "narucena_kolicina": 100}
]
narudzbe.napravi_narudzbu(proizvodi_za_dodavanje_x)

