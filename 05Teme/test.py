import random

# Cream tabla de joc, apoi o printam
tabla_joc = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(tabla_joc)
# Cream cateva variabile si functii
alegere_jucator = input("Alegeti un numar: ")
alegere_computer = random.choice(tabla_joc)
numar = int(alegere_jucator)
jucator = "x"
computer = "0"


def auto():
    while alegere_computer != jucator or computer:
        tabla_joc[alegere_computer] = int(computer)
        print("Calculatorul a ales: ")
        print(tabla_joc)
        break


def alegere():
    while numar != jucator or computer:
        tabla_joc[numar] = jucator
        print(tabla_joc)
        break


while True:
    alegere()
    auto()
