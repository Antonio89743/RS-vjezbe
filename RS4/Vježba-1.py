import asyncio
import aiohttp
import time

URL = "https://jsonplaceholder.typicode.com/users"

async def fetch_users(session):
    async with session.get(URL) as response:
        return await response.json()

async def main():
    start = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_users(session) for _ in range(5)]
        results = await asyncio.gather(*tasks)
    users = results[0]

    names = [user["name"] for user in users]
    emails = [user["email"] for user in users]
    usernames = [user["username"] for user in users]
    end = time.perf_counter()
    elapsed = end - start

    print("Imena korisnika:", names)
    print("Email adrese:", emails)
    print("Usernameovi:", usernames)
    print(f"Vrijeme izvođenja: {elapsed:.4f}s")

asyncio.run(main())
