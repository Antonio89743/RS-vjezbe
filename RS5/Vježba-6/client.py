import aiohttp
import asyncio

async def send_request(url, port):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://{url}:{port}/pozdrav') as response:
            return await response.json()

async def main():
    url = 'localhost'

    print("Sekvencijalno:")
    response1 = await send_request(url, 8081)
    print(f"Service 8081: {response1}")

    response2 = await send_request(url, 8082)
    print(f"Service 8082: {response2}")

    print("Konkurentno:")
    responses = await asyncio.gather(
        send_request(url, 8081),
        send_request(url, 8082)
    )

    print(f"Service 8081: {responses[0]}")
    print(f"Service 8082: {responses[1]}")

asyncio.run(main())
