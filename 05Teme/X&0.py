import random

tabla_joc = [1, 2, 3, 4, 5, 6, 7, 8, 9]
jucator = "X"
computer = "0"
print(tabla_joc)


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


def variante_castig():
    if tabla_joc[0] == tabla_joc[1] == tabla_joc[2]:
        if tabla_joc[0] == jucator:
            print("Ai castigat! ")
            exit()
        else:
            print("Ai pierdut! ")
    if tabla_joc[3] == tabla_joc[4] == tabla_joc[5]:
        if tabla_joc[3] == jucator:
            print("Ai castigat! ")
            exit()
        else:
            print("Ai pierdut! ")
            exit()
    if tabla_joc[6] == tabla_joc[7] == tabla_joc[8]:
        if tabla_joc[6] == jucator:
            print("Ai castigat! ")
            exit()
        else:
            print("Ai pierdut! ")
            exit()
    if tabla_joc[0] == tabla_joc[4] == tabla_joc[8]:
        if tabla_joc[0] == jucator:
            print("Ai castigat! ")
            exit()
        else:
            print("Ai pierdut! ")
            exit()
    if tabla_joc[2] == tabla_joc[4] == tabla_joc[6]:
        if tabla_joc[2] == jucator:
            print("Ai castigat! ")
            exit()
        else:
            print("Ai pierdut! ")
            exit()
    if tabla_joc[0] == tabla_joc[3] == tabla_joc[6]:
        if tabla_joc[0] == jucator:
            print("Ai castigat! ")
            exit()
        else:
            print("Ai pierdut! ")
            exit()
    if tabla_joc[1] == tabla_joc[4] == tabla_joc[7]:
        if tabla_joc[1] == jucator:
            print("Ai castigat! ")
            exit()
        else:
            print("Ai pierdut! ")
            exit()
    if tabla_joc[2] == tabla_joc[5] == tabla_joc[8]:
        if tabla_joc[2] == jucator:
            print("Ai castigat! ")
            exit()
        else:
            print("Ai pierdut! ")
            exit()


while True:
    afiseaza_alegere_jucator()
    afiseaza_alegere_computer()
    variante_castig()
