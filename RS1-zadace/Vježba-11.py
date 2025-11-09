def grupiraj_po_paritetu(lista):
    parni = [x for x in lista if x % 2 == 0]
    neparni = [x for x in lista if x % 2 != 0]
    return {'parni': parni, 'neparni': neparni}


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(grupiraj_po_paritetu(lista))