from aiohttp import web

async def umnozak_handler(request):
    try:
        data = await request.json()
        brojevi = data.get('brojevi', [])
        if not brojevi:
            return web.json_response({"error": "Nema brojeva u zahtjevu"}, status=400)
        
        umnozak = 1
        for broj in brojevi:
            umnozak *= broj
        
        return web.json_response({"umnozak": umnozak})
    
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)

app = web.Application()
app.router.add_post('/umnozak', umnozak_handler)

web.run_app(app, port=8084)
