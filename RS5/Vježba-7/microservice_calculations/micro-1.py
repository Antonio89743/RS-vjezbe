from aiohttp import web

async def zbroj_handler(request):
    try:
        data = await request.json()
        brojevi = data.get('brojevi', [])
        if not brojevi:
            return web.json_response({"error": "Nema brojeva u zahtjevu"}, status=400)
        
        zbroj = sum(brojevi)
        return web.json_response({"zbroj": zbroj})
    
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)

app = web.Application()
app.router.add_post('/zbroj', zbroj_handler)

web.run_app(app, port=8083)
