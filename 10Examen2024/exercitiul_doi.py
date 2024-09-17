tuple_example = (-1, 3, -2, 4, 0)


def numara_elemente_pozitive(lista):
    lista_pozitiva = []
    for i in lista:
        if i > 0:
            lista_pozitiva.append(i)
    print(len(lista_pozitiva))


numara_elemente_pozitive([1, -5, -9, 1, 5, 67, -39, 0])
numara_elemente_pozitive(tuple_example)