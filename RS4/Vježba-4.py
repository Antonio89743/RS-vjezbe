import asyncio

korisnici = {
    "korisnik1": "lozinka1",
    "korisnik2": "lozinka2",
    "korisnik3": "lozinka3",
}

# async def autentifikacija(username, password):
#     await asyncio.sleep(2)
    
#     if korisnici.get(username) == password:
#         print("OK")
#         return True
#     else:
#         print("ERROR")
#         raise ValueError(f"Neuspješna autentifikacija za korisnika: {username}")

async def autentifikacija(username, password):
    await asyncio.sleep(3)
    
async def main():

    # tasks = [
    #     autentifikacija("korisnik1", "lozinka1"),
    #     autentifikacija("korisnik2", "sadasdasd"),
    #     autentifikacija("korisnik3", "lozinka3"),
    #     autentifikacija("dsdasdas", "sdasdasda"),
    #     autentifikacija("korisnik1", "dsadasdas")
    # ]

    tasks = [
        asyncio.wait_for(autentifikacija("korisnik1", "lozinka1"), timeout=2),
        asyncio.wait_for(autentifikacija("korisnik2", "sadasdasd"), timeout=2),
        asyncio.wait_for(autentifikacija("korisnik3", "lozinka3"), timeout=2),
        asyncio.wait_for(autentifikacija("dsdasdas", "sdasdasda"), timeout=2),
        asyncio.wait_for(autentifikacija("korisnik1", "dsadasdas"), timeout=2)
    ]
    try:
        results = await asyncio.gather(*tasks)
    except asyncio.TimeoutError:
        print("A timeout occurred while fetching camera data.")

# Kako se ponaša asyncio.gather() kada se dogodi iznimka u jednoj od korutina?
    # Exception has occurred: ValueError

asyncio.run(main())
