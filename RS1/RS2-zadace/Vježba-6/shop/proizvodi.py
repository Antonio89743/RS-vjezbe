class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}")
        print(f"Cijena: {self.cijena}")
        print(f"Dostupna količina: {self.dostupna_kolicina}")


def dodaj_proizvod(proizvod):
    skladiste.append(proizvod)

skladiste: list[Proizvod] = []

proizvod_1: Proizvod = Proizvod("Laptop", 1500.00, 10)
dodaj_proizvod(proizvod_1)
proizvod_2: Proizvod = Proizvod("Mobitel", 800.00, 25)
dodaj_proizvod(proizvod_2)

