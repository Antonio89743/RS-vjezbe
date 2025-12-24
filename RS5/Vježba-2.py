from aiohttp import web

proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "količina": 10},
    {"naziv": "Tablet", "cijena": 1500, "količina": 15},
]

async def proizvodi_handler(request):
    return web.json_response(proizvodi)

async def dodaj_proizvod_handler(request):
    novi_proizvod = await request.json()
    proizvodi.append(novi_proizvod)
    return web.json_response(proizvodi, status=201)

async def main():
    app = web.Application()
    app.router.add_get('/proizvodi', proizvodi_handler)
    app.router.add_post('/proizvodi', dodaj_proizvod_handler)
    return app

web.run_app(main(), port=8081)
