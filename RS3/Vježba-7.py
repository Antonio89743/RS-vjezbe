import asyncio

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]

    await asyncio.gather(*timers)

asyncio.run(main())




# timer funkcija kreće s izvršavanjem po redosljedu zadanom u listi timers
# izvršava timer 1, timer 2 i timer 3 paralelno, odizimajući 1 sekundu od preostalih sekundi tog timer delay integera
# kako je timer 1 najkraći, on prvi završava, a ostali timeri i dalje nastavljaju s odbrojavanjem, izmjenično ispisuju preostale sekunde za timer 2 i 3
# sljedeći završen timer je timer 2
# preostali timer 3 nastavlja s izvođenjem dok ne dođe do nule
# tada su svi timeri završeni

 

# Timer 1: 3 sekundi preostalo...
# Timer 2: 5 sekundi preostalo...
# Timer 3: 7 sekundi preostalo...
# Timer 1: 2 sekundi preostalo...
# Timer 2: 4 sekundi preostalo...
# Timer 3: 6 sekundi preostalo...
# Timer 1: 1 sekundi preostalo...
# Timer 2: 3 sekundi preostalo...
# Timer 3: 5 sekundi preostalo...
# Timer 1: Vrijeme je isteklo!
# Timer 2: 2 sekundi preostalo...
# Timer 3: 4 sekundi preostalo...
# Timer 2: 1 sekundi preostalo...
# Timer 3: 3 sekundi preostalo...
# Timer 2: Vrijeme je isteklo!
# Timer 3: 2 sekundi preostalo...
# Timer 3: 1 sekundi preostalo...
# Timer 3: Vrijeme je isteklo!



# asyncio.run(main()) pokreće main() funkciju event loop-a
# timers lista koristi asyncio.create_task() kako bi se kreirale i pokrenule tri async timer zadaci
# asyncio.gather(*timers) čeka da svi zadaci u timers listi budu dovršeni prije nego što nastavi dalje
# await asyncio.gather(*timers) završava main() funkciju jednom kad su svi zadaci dovršeni

# timer funkcije će se obavljati konkurentno, pa će prvi završiti timer 1, zatim timer 2, a na kraju timer 3
# za vrijeme izvođenja timer funkcija, funkcije će predati kontrolu event loop-u koristći sleep(), event loop čeka da se timer funckije izvrše
