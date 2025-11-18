import asyncio

async def secure_data(data: dict):
    await asyncio.sleep(3)
    return {
        'prezime': data['prezime'], 
        'broj_kartice': hash(data['broj_kartice']),
        'CVV': hash(data['CVV'])
        }

async def main():
    data = [
        {
            "prezime": "AAAA",
            "broj_kartice": 0,
            "CVV": 123
            },
        {
            "prezime": "BBBB",
            "broj_kartice": 1,
            "CVV": 456
            },
        {
            "prezime": "CCCC",
            "broj_kartice": 2,
            "CVV": 789
            }
    ]
    zadaci = [asyncio.create_task(secure_data(data_entry)) for data_entry in data]
    rezultati = await asyncio.gather(*zadaci)
    print("Rezultati:")
    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())