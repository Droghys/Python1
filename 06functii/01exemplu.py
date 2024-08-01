# print("Mesaj")
# input("Adauga un numar: ")

def my_function(nr_mere: str, nume: str) -> (str, str):
    return f"{nume} are {nr_mere} mere", f"{nume} are {nr_mere} pere"


a, c = my_function("2", "Ana")
b, d = my_function("3", "Maria")
print(a)
print(b)
print(c)
print(d)
