# format_cnp = ['S', 'AA', 'LL', 'ZZ', 'JJ', 'NNN', 'C']
CNP = input("Introduceti CNP: ")
# my_cnp = "2791463582790"
for value in CNP:
    if len(CNP) > 13:
        print("CNP-ul este prea lung")
        break
