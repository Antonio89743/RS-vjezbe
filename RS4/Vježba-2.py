import asyncio
import aiohttp

URL = "https://catfact.ninja/fact"

async def get_cat_fact(session):
    async with session.get(URL) as response:
        data = await response.json()
        return data["fact"]

async def filter_cat_facts(facts):
    return [fact for fact in facts if "cat" in fact.lower() or "cats" in fact.lower()]

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(20)]
        facts = await asyncio.gather(*tasks)
    filtered_facts = await filter_cat_facts(facts)
    print("Filtrirane činjenice o mačkama:")
    for f in filtered_facts:
        print("-", f)

asyncio.run(main())
