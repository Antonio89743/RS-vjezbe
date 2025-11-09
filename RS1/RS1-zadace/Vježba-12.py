def obrni_rjecnik(rjecnik):
    return {v: k for k, v in rjecnik.items()}


rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

print(obrni_rjecnik(rjecnik))