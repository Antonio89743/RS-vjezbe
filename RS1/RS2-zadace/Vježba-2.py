# Zadatak 1

nizovi = ["jabuka", "kruška", "banana", "naranča"]

kvadrirane_duljine = list(map(lambda s: len(s) ** 2, nizovi))

print(kvadrirane_duljine)

# Zadatak 2

brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]

veci_od_5 = list(filter(lambda x: x > 5, brojevi))

print(veci_od_5)



# Zadatak 3

brojevi = [10, 5, 12, 15, 20]

transform = dict(map(lambda x: (x, x**2), brojevi))

print(transform)



# Zadatak 4

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18}
]

svi_punoljetni = all(map(lambda student: student['godine'] >= 18, studenti))

print(svi_punoljetni)



# Zadatak 5

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]

min_duljina = input("Unesite minimalnu duljinu riječi: ")

duge_rijeci = list(filter(lambda rijec: len(rijec) >= int(min_duljina), rijeci))

print(duge_rijeci)