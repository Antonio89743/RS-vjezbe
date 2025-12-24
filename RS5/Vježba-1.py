from aiohttp import web

proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "količina": 10},
    {"naziv": "Tablet", "cijena": 1500, "količina": 15},
]

async def proizvodi_handler(request):
    return web.json_response(proizvodi)

async def main():
    app = web.Application()
    app.router.add_get('/proizvodi', proizvodi_handler)
    return app

web.run_app(main(), port=8081)
