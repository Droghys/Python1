# """
# r -> citire, nu adauga, este valoarea default, daca fisierul
#     nu exista apare eroare
# w -> scriere, daca fisierul nu exista, il adauga,
#     daca exista informatie in fisier, aceasta este rescrisa
# a -> scriere, daca exista informatie in fisier, adauga, nu rescrie
# r+ -> scriere, citire, daca fisierul nu exista, apare eroare
# """
# file = open('data.txt', 'r+')
# file.write("hello\n")
# file.close()
#
# file = open('data.txt', 'a')
# file.write("hello1\n")
# file.close()
#
# with open('data.txt', 'w') as file:
#     file.write("hello")

with open('data.txt', 'r') as file:
    for line in file.readlines():
        print(line)

with open('data.txt', 'r') as unicorn:
    while True:
        line = unicorn.readline()
        if not line:
            break
        print(line)


def add_task():
    lista_task = []
    task = input("Intorduceti task ul: ")
    while True:
        timp_limit = input("Introduceti data limita in format dd.mm.yyyy: ")
        try:
            time.strptime(timp_limit, "%d.%m.%Y")
            break
        except ValueError:
            print("Data nu este valida. Incercati din nou")

    pers_responsabila = input("Perosana care se va ocupa de task: ")
    categ_task = input("Din ce categorie face parte task ul?: ")
    lista_task.append(task)
    lista_task.append(timp_limit)
    lista_task.append(pers_responsabila)
    lista_task.append(categ_task)
    with open("task_uri.txt", "a") as task_uri:
        # task_a = task_uri.readline()
        print(f"Task: {lista_task[0]}: {lista_task[1]}: {lista_task[2]}")
        with open("categori.txt", "r") as categ:
            r_cat = [line.strip() for line in categ.readlines()]
            # print(r_cat)
            if categ_task not in r_cat:
                print("Nu exista aceasta categorie")
                add_categori()
            else:
                for element in lista_task:
                    # task_a.writerow(element)
                    task_uri.write(element)
                    task_uri.write(": ")
                task_uri.write("\n")