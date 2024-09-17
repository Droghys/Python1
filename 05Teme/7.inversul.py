"""7.
scrieti un program care sa extraga inversul dintr
un nr.
Exemplu: 7536 trebuie afisati 6 3 5 7"""


numar = list(input("Adaugati un numar: "))

if len(numar) > 1:
    (numar.reverse())
print(numar)
