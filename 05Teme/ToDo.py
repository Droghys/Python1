import time


def meniu():                  # Functia meniu
    while True:
        print("------------------------------------------")
        print(" 1.Listare date")
        print(" 2.Sortare")
        print(" 3.Filtrare date")
        print(" 4.Adauga unu nou task în lista inițială")
        print(" 5.Editarea detaliilor referitoare la task")
        print(" 6.Ștergerea unui task din lista inițială")
        print(" 7.Exit")
        print("------------------------------------------")

        aleg = int(input("\n + Alegeti o optiune: "))
        if aleg == 4:
            time.sleep(2)
            adauga()
        elif aleg == 1:
            print("    Categoriile sortate:")
            sort_categorii()
            print("                                   ")
            time.sleep(2)
        elif aleg == 2:
            sortare()
        elif aleg == 3:
            filtrare_date()
        elif aleg == 6:
            stergere_task()
        elif aleg == 7:
            break


def adauga():              # Functia pentru adaugare
    lista_taskuri = []
    task = input("Adauga un task: ")
    persoana = input("Desemnati o persoana pentru task: ")
    data = input("Alegeti o data limita pentru task: ")
    categorie = input("Alegeti categoria pentru task: ")

    lista_taskuri.append(task)
    lista_taskuri.append(persoana)
    lista_taskuri.append(data)
    lista_taskuri.append(categorie)

    # Verifica daca exista categoria
    with open("categorii.txt", "r") as file:
        categorii = [line.strip() for line in file]

    if categorie not in categorii:
        print("Nu exista aceasta categorie")
        adaos = input("Adaugati o categorie: ")
        if adaos not in categorii:
            with open('categorii.txt', 'a') as file:
                file.write(adaos + "\n")

    # Import in fisierul text
    with open("task_list.txt", "a") as file:
        for element in lista_taskuri:
            file.write(element + " ->")
        file.write("\n")


def sort_categorii():         # Functia de sortare
    with open("categorii.txt", 'r') as file:
        linii = [line.strip() for line in file]
    linii.sort()
    print(linii)


def sortare():
    print("Criteriile disponibile sunt: ")
    print("1. sortare ascendentă task")
    print("2. sortare descendentă task")
    print("3. sortare ascendentă data")
    print("4. sortare descendentă data")
    print("5. sortare ascendentă persoana responsabilă")
    print("6. sortare descendentă persoană responsabilă")
    print("7. sortare ascendentă categorie")
    print("8. sortare descendentă categorie")

    alegere = int(input("\n + Alegeți criteriul de sortare: "))

    with open("task_list.txt", "r") as file:
        linii = [line.strip().split(" ->") for line in file]

    if alegere == 1:
        sorted_list = sorted(linii)
    elif alegere == 2:
        sorted_list = sorted(linii, reverse=True)
    elif alegere == 3:
        sorted_list = sorted(linii)
    elif alegere == 4:
        sorted_list = sorted(linii, reverse=True)
    elif alegere == 5:
        sorted_list = sorted(linii)
    elif alegere == 6:
        sorted_list = sorted(linii, reverse=True)
    elif alegere == 7:
        sorted_list = sorted(linii)
    elif alegere == 8:
        sorted_list = sorted(linii, reverse=True)
    else:
        print("Alegere invalida!")
        return

    for item in sorted_list:
        print(" -> ".join(item))


def filtrare_date():
    with open("task_list.txt", "r") as file:
        linii = [line.strip().split(" ->") for line in file]
    filtru = input("Alegeti un criteriu de filtrare\nExemple: Task, Persoana, Data, Categorie: ")
    filtru_modificat = filtru.lower()

    if filtru_modificat == "task":
        for linie in linii:
            print(linie[0])
    elif filtru_modificat == "persoana":
        for linie in linii:
            print(linie[1])
    elif filtru_modificat == "data":
        for linie in linii:
            print(linie[2])
    elif filtru_modificat == "categorie":
        for linie in linii:
            print(linie[3])
    else:
        print("Alegere indisponibila: ")
        return


def stergere_task():
    with open("task_list.txt", "r") as file:
        linii = [line.strip().split(" ->") for line in file]
    for index, line in enumerate(linii, start=1):
        print(f"{index}: {line}")
    stergere = int(input("Alegeti task pentru stergere: "))
    if stergere < 0 < len(linii):
        linii.pop(stergere)


meniu()
