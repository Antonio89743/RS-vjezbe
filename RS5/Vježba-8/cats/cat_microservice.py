import aiohttp
from aiohttp import web

CAT_FACTS_API = "https://catfact.ninja/facts"

async def fetch_cat_facts(amount: int):
    async with aiohttp.ClientSession() as session:
        params = {'limit': amount}
        async with session.get(CAT_FACTS_API, params=params) as response:
            data = await response.json()
            return [fact['fact'] for fact in data['data']]

async def handle_get_cat_amount(request):
    amount = int(request.match_info['amount'])
    facts = await fetch_cat_facts(amount)
    return web.json_response({'facts': facts})

app = web.Application()
app.router.add_get('/cat/{amount}', handle_get_cat_amount)

web.run_app(app, port=8086)
