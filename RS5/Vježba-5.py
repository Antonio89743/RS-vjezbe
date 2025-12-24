import asyncio
import aiohttp
from aiohttp import web

narudzbe = []

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

async def proizvodi_handler(request):
    return web.json_response(proizvodi)

async def proizvod_by_id_handler(request):
    proizvod_id = int(request.match_info['id'])
    proizvod = next((p for p in proizvodi if p['id'] == proizvod_id), None)
    if proizvod:
        return web.json_response(proizvod)
    else:
        return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)

async def narudzbe_handler(request):
    data = await request.json()
    proizvod_id = data['proizvod_id']
    kolicina = data['kolicina']
    
    proizvod = next((p for p in proizvodi if p['id'] == proizvod_id), None)
    
    if proizvod:
        nova_narudzba = {'proizvod_id': proizvod_id, 'kolicina': kolicina}
        narudzbe.append(nova_narudzba)
        return web.json_response(narudzbe, status=201)
    else:
        return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)

async def run():
    app = web.Application()
    app.router.add_get('/proizvodi', proizvodi_handler)
    app.router.add_get('/proizvodi/{id}', proizvod_by_id_handler)
    app.router.add_post('/narudzbe', narudzbe_handler) 
    return app

web.run_app(run(), port=8081)

async def test_server():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8081/proizvodi') as response:
            print("GET /proizvodi - Status:", response.status)
            proizvodi = await response.json()
            print(proizvodi)

        async with session.get('http://localhost:8081/proizvodi/1') as response:
            print("GET /proizvodi/1 - Status:", response.status)
            proizvod = await response.json()
            print(proizvod)

        async with session.get('http://localhost:8081/proizvodi/99') as response:
            print("GET /proizvodi/99 - Status:", response.status)
            error_message = await response.json()
            print(error_message)

        async with session.post('http://localhost:8081/narudzbe', json={"proizvod_id": 1, "kolicina": 2}) as response:
            print("POST /narudzbe - Status:", response.status)
            narudzbe_data = await response.json()
            print("Narudžbe:", narudzbe_data)

        async with session.post('http://localhost:8081/narudzbe', json={"proizvod_id": 99, "kolicina": 2}) as response:
            print("POST /narudzbe - Status:", response.status)
            error_message = await response.json()
            print("Greška za nepostojeći proizvod:", error_message)

async def main():
    app = await run()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8081)
    await site.start()
    await test_server()
    await runner.cleanup()

asyncio.run(main())
