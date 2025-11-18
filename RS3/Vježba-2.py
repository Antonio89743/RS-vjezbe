import asyncio

async def get_users():
    await asyncio.sleep(3)
    users = [
        {"id": i, "Ime": f"Korisnik{i}", "E-mail": f"user{i}@test.com"}
        for i in range(5)
    ]
    return users

async def get_products():
    await asyncio.sleep(5)
    proizvodi = [
        {"id": i, "Ime": f"Proizvod {i}", "Cijena": i - .01}
        for i in range(2)
    ]
    return proizvodi

async def run():
    users, productss = await asyncio.gather(
        get_users(),
        get_products()
    )
    print("Korisnici:", users)
    print("Proizvodi:", productss)

asyncio.run(run()) 