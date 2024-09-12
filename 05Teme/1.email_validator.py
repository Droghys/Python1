"""
1.
Creati un program in care utilizatorul sa introduca o adresa de email de formatul
litere_sau_cifre@litere_sau_cifre.litere.
a.  Validati acest sir de caractere si informati utilizatorul de raspuns. @ sau .(punct) trebuie sa
exista o singura data
in sirul de caractere
b. trebuie sa contina @ si . o singura data
c. tot ce este inainte de . contine litere_sau_cifre, cu exceptia @
d. tot ce urmeaza dupa . contine doar litere
e. trebuie sa avem caracter scris inainte de @
f. trebuie sa avem caracter(e)
scris(e) intre @ si .
g. trebuie sa avem minim 2 litere dupa .
"""

adresa = input("Introduceti adresa de email: ")
numar_aron = adresa.count("@")
numar_punct = adresa.count(".")
stanga, dreapta = adresa.split(".", 1)


def a_b():
    if "@" not in adresa or "." not in adresa:
        print("Email-ul trebuie sa contina '@' si .(punct) ")
    elif numar_aron > 1:
        print("Email-ul contine '@' de prea multe ori")
    elif numar_punct > 1:
        print("Email-ul contine '.(punct)' de prea multe ori")


def d():
    if dreapta.isalpha() == True:
        print("Email-ul dupa .(punct) trebuie sa contina doar litere")


a_b()
d()
