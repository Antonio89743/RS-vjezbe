def run():
    broj_1_str = input("Unesite prvi broj: ").strip()
    broj_2_str = input("Unesite drugi broj: ").strip()
    operator = input("Unesite operator: ").strip()

    try:
        broj_1 = float(broj_1_str)
        broj_2 = float(broj_2_str)
    except ValueError:
        print("Greška: Unesite validne brojeve!")
        return
    if operator not in "+-*/":
        print("Nepodržani operator!")
        return
    namespace = {}

    try:
        exec(f"resultat = {broj_1} {operator} {broj_2}", namespace)
        resultat = namespace['resultat']
    except ZeroDivisionError:
        print("Dijeljenje s nulom nije dozvoljeno!")
        return
    print(f"Rezultat operacije {broj_1} {operator} {broj_2} je {resultat}")


run()
