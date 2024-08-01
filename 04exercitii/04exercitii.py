"""
1. Sa se verifice daca textul introdus de la tastatura de catre un utilizator este un sir de
caractere de tip string sau un sir de numere. Utilizati instructiunea de tip if-elif-else.
In cazul in care valoarea este un sir de caractere, afisati pe ecran mesajul “Sirul de
caractere a fost gasit de Mihai”, unde Mihai reprezinta numele vostru
preluat automat de la tastatura.
"""
text_utilizator = input("Introduceti textul: ")
variabila_test_string = True
for i in text_utilizator:
    if i in "0123456789":
        variabila_test_string = False
        break
print(variabila_test_string)
if variabila_test_string is True:
    print("Sir de caractere")
else:
    print("Sir de caractere si cifre")

"""
2. Creati un program in care utilizatorul sa introduca un numar. Validati daca acest
numar este par sau impar si afisati un raspuns in acest sens.
"""
cifra = int(input("Introduceti un numar:"))
if cifra % 2 == 0:
    print("Numarul este par")
else:
    print("Numarul este impar")

    """
    3. Creati un program in care utilizatorul sa introduca un an. Calculati daca anul este
    bisect sau nu si afisati un raspuns in acest sens. OBS. Un an bisect se imparte exact
    la 4 (fara rest)
    """
    an = input("introduceti un an: ")
    if int(an) % 4 == 0:
        print("anul este bisect")
    else:
        print("anul nu este bisect")

"""
4. Creati un program in care utilizatorul sa introduca un numar. Calculati daca numarul
este pozitiv, zero sau negativ. In cazul in care este pozitiv validati daca este mai mic
decat 10 si afisati un mesaj de confirmare..Daca numarul este zero afisati “Numarul
este 0”, iar daca numarul este negativ atunci transformati numarul in numar pozitiv si
afisati numarul pozitiv.
"""
variabila = int(input("Numar: "))
if variabila > 0:
    print("Numarul este pozitiv")
    if variabila < 10:
        print("Numarul este mai mic ca 10")
elif variabila < 0:
    print("Numarul este negativ")
    variabila = variabila * -1
    print(variabila)
else:
    print("Numarul este 0")
