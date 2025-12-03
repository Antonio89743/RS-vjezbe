import asyncio
import aiohttp

async def fetch_url(session, url: str) -> str:
    async with session.get(url, timeout=5) as response:
        return await response.text()

async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://api.github.com"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch_url(session, url)) for url in urls]
        results = await asyncio.gather(*tasks)
        for url, content in zip(urls, results):
            print(f"Fetched {len(content)} characters from {url}")

if __name__ == "__main__":
    asyncio.run(main())
