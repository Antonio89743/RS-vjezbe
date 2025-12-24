from aiohttp import web

async def handle_post_facts(request):
    data = await request.json()
    facts = data.get('facts', [])
    valid_facts = [fact for fact in facts if 'cat' in fact.lower()]
    return web.json_response({'valid_facts': valid_facts})

app = web.Application()
app.router.add_post('/facts', handle_post_facts)

web.run_app(app, port=8087)
