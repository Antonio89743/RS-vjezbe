from aiohttp import web

korisnici = [
    {'ime': 'Ivo', 'godine': 25},
    {'ime': 'Ana', 'godine': 17},
    {'ime': 'Marko', 'godine': 19},
    {'ime': 'Maja', 'godine': 16},
    {'ime': 'Iva', 'godine': 22}
]

def filter(korisnici):
    return [korisnik for korisnik in korisnici if korisnik['godine'] > 18]

async def punoljetni_handler(request):
    punoljetni_korisnici = filter(korisnici)
    return web.json_response(punoljetni_korisnici)

async def main():
    app = web.Application()
    app.router.add_get('/punoljetni', punoljetni_handler)
    return app

web.run_app(main(), port=8082)
