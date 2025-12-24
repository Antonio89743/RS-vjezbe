import aiohttp
import asyncio

CAT_MICROSERVICE_URL = "http://localhost:8086/cat"
CAT_FACT_CHECK_URL = "http://localhost:8087/facts"

async def fetch_cat_facts(amount: int):
    async with aiohttp.ClientSession() as session:
        url = f"{CAT_MICROSERVICE_URL}/{amount}"
        async with session.get(url) as response:
            data = await response.json()
            return data['facts']

async def check_facts(facts: list):
    async with aiohttp.ClientSession() as session:
        async with session.post(CAT_FACT_CHECK_URL, json={'facts': facts}) as response:
            data = await response.json()
            return data['valid_facts']

async def main():
    amount = 10
    facts = await fetch_cat_facts(amount)
    print("Fetched Facts:", facts)
    
    valid_facts = await check_facts(facts)
    print("Valid Facts:", valid_facts)

asyncio.run(main())
