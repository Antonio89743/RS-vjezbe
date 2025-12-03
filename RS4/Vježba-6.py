import asyncio
import random

async def fetch_weather_data(station_id: int) -> float:
    delay = random.uniform(1, 5)
    await asyncio.sleep(delay)
    return random.uniform(20, 25)

async def main():
    tasks = []
    for i in range(1, 11):
        task = asyncio.create_task(
            asyncio.wait_for(fetch_weather_data(i), timeout=2)
        )
        tasks.append(task)

    results = await asyncio.gather(*tasks, return_exceptions=True)

    valid_temps = []
    for station_id, result in enumerate(results, start=1):
        if isinstance(result, asyncio.TimeoutError):
            print(f"Stanica {station_id} nije odgovorila na vrijeme (timeout).")
        else:
            print(f"Stanica {station_id}: {result} °C")
            valid_temps.append(result)

    if valid_temps:
        print(f"Prosječna temperatura: {(sum(valid_temps) / len(valid_temps))} °C")

asyncio.run(main())
