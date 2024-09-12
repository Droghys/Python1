import random

tabla_joc = [1, 2, 3, 4, 5, 6, 7, 8, 9]
jucator = "X"
computer = "0"
print(tabla_joc)


def variante_castig():
    variante = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6)]
    for optiune in variante:
        if tabla_joc[optiune[0]] == tabla_joc[optiune[1]] == tabla_joc[optiune[2]]:
            if tabla_joc[optiune[0]] == jucator:
                print("Ai castigat! ")
                exit()
        elif tabla_joc[optiune[0]] == computer:
            print("Ai pierdut! ")
            exit()


def afiseaza_alegere_jucator():
    alegere_jucator = int(input("Alegeti un numar: "))
    if alegere_jucator in tabla_joc:
        tabla_joc[alegere_jucator - 1] = jucator
        print("-----------------------------")
        print(tabla_joc)
        print("-----------------------------")
    else:
        print("Numărul ales nu este disponibil.")
    return tabla_joc


def afiseaza_alegere_computer():
    optiuni_disponibile = [pos for pos in tabla_joc if pos in range(1, 10)]
    if optiuni_disponibile:
        alegere_computer = random.choice(optiuni_disponibile)
        tabla_joc[alegere_computer - 1] = computer
        print("-----------------------------")
        print(tabla_joc)
        print("-----------------------------")
    else:
        print("Nu mai sunt opțiuni disponibile.")
    return tabla_joc


while True:
    afiseaza_alegere_jucator()
    afiseaza_alegere_computer()
    variante_castig()
