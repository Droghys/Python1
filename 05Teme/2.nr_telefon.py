"""2.
Scrieti un program care sa valideze nr de telefon al unui utilizator scris de la tastatura.
+40123456789
-
> incepe cu +40 (primele 3 caractere sunt +40)
-
> are 12 caractere
-
> sa aiba caracterele de la 3 la 12 sa fie doar cifre"""

nr_telefon = str(input("Introduceti numarul de telefon: "))

if nr_telefon[0:3] != "+40":
    print("Numarul de telefon trebuie sa inceapa cu +40")
elif len(nr_telefon) != 12:
    print("Numarul de telefon trebuie sa contina 12 cifre")
elif not nr_telefon[3:].isdigit():
    print("Numarul de telefon trebuie sa contina doar cifre")
else:
    print(f" Numar Valid: {nr_telefon}")
