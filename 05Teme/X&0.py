import random

# Cream tabla de joc, apoi o printam
tabla_joc = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(tabla_joc)

# Cream cateva variabile si functii
alegere_jucator = int(input("Alegeti un numar: "))
alegere_computer = random.choice(tabla_joc)
numar = alegere_jucator
jucator = "X"
computer = "O"


def auto():
    tabla_joc[alegere_computer] = computer
    print("Calculatorul a ales: ")
    print(tabla_joc)


# Incepem jocul facand prima alegere
if numar in tabla_joc:
    tabla_joc[numar] = jucator
    print(tabla_joc)
else:
    print("Numărul ales nu este disponibil.")
