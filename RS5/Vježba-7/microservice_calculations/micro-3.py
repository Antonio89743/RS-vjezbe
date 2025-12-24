from aiohttp import web

async def kolicnik_handler(request):
    try:
        data = await request.json()
        zbroj = data.get('zbroj')
        umnozak = data.get('umnozak')

        if zbroj is None or umnozak is None:
            return web.json_response({"error": "Zbroj ili umnozak nisu proslijeđeni"}, status=400)

        if zbroj == 0:
            return web.json_response({"error": "Podjela s nulom nije moguća"}, status=400)

        kolicnik = umnozak / zbroj
        return web.json_response({"kolicnik": kolicnik})

    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)

app = web.Application()
app.router.add_post('/kolicnik', kolicnik_handler)

web.run_app(app, port=8085)
