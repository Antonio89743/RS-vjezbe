# Zadatak 1

def prvi_i_zadnji(lista):
    return lista[0], lista[-1]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Prvi i zadnji")
print(prvi_i_zadnji(lista))



# Zadatak 2

def maks_i_min(lista):
    for i in range(len(lista)):
        if i == 0:
            maks = lista[i]
            min = lista[i]
        else:
            if lista[i] > maks:
                maks = lista[i]
            if lista[i] < min:
                min = lista[i]
    return  maks, min

lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print("\nMaks i min")
print(maks_i_min(lista))



# Zadatak 3

def presjek(skup_1, skup_2):
    return skup_1.intersection(skup_2)

skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
print("\nPresjek")
print(presjek(skup_1, skup_2))