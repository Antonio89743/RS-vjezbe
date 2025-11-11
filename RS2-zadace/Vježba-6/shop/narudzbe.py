from shop.proizvodi import skladiste

class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        print("Naručeni proizvodi:")
        for item in self.naruceni_proizvodi:
            print(f"Naziv: {item["naziv"]}, X {item["narucena_kolicina"]}")
        print(f"Ukupna cijena: {self.ukupna_cijena} eur")


def napravi_narudzbu(naruceni_proizvodi):
    if isinstance(naruceni_proizvodi, list) == False:
        return
    
    if len(naruceni_proizvodi) == 0:
        return
    
    for i, item in enumerate(naruceni_proizvodi):
        if isinstance(item, dict) == False:
            return
        potrebni_kljucevi = {"naziv", "cijena", "narucena_kolicina"}
        if potrebni_kljucevi.issubset(item.keys()) == False:
            return

    for item in naruceni_proizvodi:
        naziv = item["naziv"]
        narucena_kolicina = item["narucena_kolicina"]
        proizvod = next((p for p in skladiste if p.naziv == naziv), None)
        if proizvod is None:
            return
        if proizvod.dostupna_kolicina < narucena_kolicina:
            print(f"Proizvod {item["naziv"]} nije dostupan!")
            return

    ukupna_cijena = sum(item["cijena"] * item["narucena_kolicina"] for item in naruceni_proizvodi)

    for item in naruceni_proizvodi:
        naziv = item["naziv"]
        narucena_kolicina = item["narucena_kolicina"]
        proizvod = next(p for p in skladiste if p.naziv == naziv)
        proizvod.dostupna_kolicina -= narucena_kolicina

    nova_narudzba = Narudzba(naruceni_proizvodi.copy(), ukupna_cijena)
    narudzbe.append(nova_narudzba)

    nova_narudzba.ispis_narudzbe()

    return nova_narudzba

narudzbe = []