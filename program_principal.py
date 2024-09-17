from my_package.modul1 import functia_mea, my_var
from my_package.modul2 import functie_diferenta, preluare_input, my_var as variabila2


if __name__ == '__main__':
    print(functia_mea())
    print(my_var)
    print(variabila2)
    x = int(preluare_input())
    y = int(preluare_input())
    print(functie_diferenta(2, 3))
    print('de aici porneste rularea')
