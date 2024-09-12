"""6.
sa se scrie o functie care sa returneze True in cazul in care primul si ultimul element
dintr-o lista sunt la fel. Altfel, returnati False."""

lista = list(input("Alegeti o lista: "))


def truesaufalse():
    if lista[0] == lista[-1]:
        return True
    else:
        return False


print(truesaufalse())
