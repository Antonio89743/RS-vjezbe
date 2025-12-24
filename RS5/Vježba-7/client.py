import aiohttp
import asyncio

async def send_request(url, port, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'http://{url}:{port}', json=data) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Error: {response.status}, {await response.text()}")
                return None

async def main():
    url = 'localhost'

    data = {"brojevi": [1, 2, 3, 4, 5]}

    print("Konkurentno")
    response1 = send_request(url, '8083/zbroj', data)
    response2 = send_request(url, '8084/umnozak', data)

    zbroj_data, umnozak_data = await asyncio.gather(response1, response2)

    print(f"Odgovor sa servisa 8083 (zbroj): {zbroj_data}")
    print(f"Odgovor sa servisa 8084 (umnozak): {umnozak_data}")

    if zbroj_data is None or umnozak_data is None:
        print("NoneType")
        return
    if 'zbroj' in zbroj_data and 'umnozak' in umnozak_data:
        kolicnik_data = await send_request(url, '8085/kolicnik', {
            "zbroj": zbroj_data['zbroj'],
            "umnozak": umnozak_data['umnozak']
        })
        print(f"kolicnik: {kolicnik_data}")

asyncio.run(main())
