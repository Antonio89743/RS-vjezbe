# Zadatak 1

def run_zadatak_1():
    print("Zadatak 1:")
    suma = sum(range(2, 101, 2))
    print(f"Suma parnih brojeva od 1 do 100 je: {suma}")

run_zadatak_1()



# Zadatak 2

def run_zadatak_2():
    print("\nZadatak 2:")
    neparni = []
    broj = 1

    while len(neparni) < 10:
        neparni.append(broj)
        broj += 2    

    for i in range(len(neparni) - 1, -1, -1):
        print(neparni[i])

run_zadatak_2()



# Zadatak 3

def run_zadatak_3():
    print("\nZadatak 3:")
    a = 0
    b = 1
    while a <= 1000:
        print(a)
        a, b = b, a + b


run_zadatak_3()