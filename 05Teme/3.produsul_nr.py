"""3.
Se cer 2 nr intregi de la tastatura. Sa se calculeze produsul daca produsul dintre cele 2
numere este mai mic sau egal cu 1000, altfel, sa se returneze suma acestora."""

nr_1 = int(input("Adaugati primul numar: "))
nr_2 = int(input("Adaugati al doilea numar: "))

if nr_1 * nr_2 <= 1000:
    produsul = nr_1 * nr_2
    print(produsul)
else:
    adunarea = nr_1 + nr_2
    print(adunarea)
