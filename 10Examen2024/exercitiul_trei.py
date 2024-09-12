
def imparte_lista(lista):
    despartire = int(input("Alegeti idexul de impartire al listei: "))
    prima_jumatate = lista[:despartire]
    doua_jumatate = lista[despartire:]
    print(prima_jumatate)
    print(doua_jumatate)


imparte_lista([1, 2, 3, 4, 5, 6, 7, 8, 9])
