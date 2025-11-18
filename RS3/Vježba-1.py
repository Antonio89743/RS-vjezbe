import asyncio

async def get_web_data():
    await asyncio.sleep(3)
    data = [i for i in range(1, 11)]
    print("Podaci dohvaćeni.", data)
    return data

asyncio.run(get_web_data())