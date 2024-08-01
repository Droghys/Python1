cuvant = "onomatopee".lower()
cuvant_de_ghicit = list(cuvant)
for index, valoare in enumerate(cuvant):
    print(index, valoare)
    if cuvant[0] != valoare and cuvant[-1] != valoare:
        cuvant_de_ghicit[index] = '_'
cuvant_de_ghicit = ' '.join(cuvant_de_ghicit)
print(cuvant_de_ghicit)
numar_vieti = 7
while numar_vieti > 0:
    litera = input("Alege o litera: ").lower()
    if len(litera) > 1 or litera in '0123456789':
        print("Introduceti o singura litera si nu cifre")
        continue
    elif litera in cuvant:
        print('se afla', litera)
        cuvant_de_ghicit = list("".join(cuvant_de_ghicit).replace(" ", ""))
        for index, valoare in enumerate(cuvant):
            if litera == valoare:
                cuvant_de_ghicit[index] = litera
        cuvant_de_ghicit = " ".join(cuvant_de_ghicit)
        print(cuvant_de_ghicit)

        if "".join(cuvant_de_ghicit) == cuvant or "_" not in cuvant_de_ghicit:
            print(f"Ai castigat! Cuvantul era: {cuvant}")
            break
    else:
        numar_vieti = numar_vieti - 1
        if numar_vieti <= 0:
            print(f"Ai pierdut! Cuvantul era:{cuvant}")
