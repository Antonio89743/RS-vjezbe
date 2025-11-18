import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autorizacija(db_user: dict, password: str):
    await asyncio.sleep(2)
    for entry in baza_lozinka:
        if entry["korisnicko_ime"] == db_user["korisnicko_ime"]:
            if entry["lozinka"] == password:
                print(f"Korisnik {db_user['korisnicko_ime']}: Autorizacija uspješna.")
            else:
                print(f"Korisnik {db_user['korisnicko_ime']}: Autorizacija neuspješna.")
            return

async def autentifikacija(user_dict: dict):
    if not all(key in user_dict for key in ["korisnicko_ime", "email", "lozinka"]):
        return
    
    await asyncio.sleep(3)
    
    pronadeni_korisnik = None
    for korisnik in baza_korisnika:
        if (korisnik["korisnicko_ime"] == user_dict["korisnicko_ime"] and
            korisnik["email"] == user_dict["email"]):
            pronadeni_korisnik = korisnik
            break
    
    if not pronadeni_korisnik:
        print(f"Korisnik {user_dict['korisnicko_ime']} nije pronađen.")
        return
    
    await autorizacija(pronadeni_korisnik, user_dict["lozinka"])

async def main():
    await autentifikacija({
        "korisnicko_ime": "ana_anic",
        "email": "aanic@gmail.com",
        "lozinka": "super_teska_lozinka"
    })

asyncio.run(main())