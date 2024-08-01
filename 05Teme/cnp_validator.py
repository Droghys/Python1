# Format: SAALLZZJJNNNC
s = range(1, 9)
aa = range(0, 100)
ll = range(1, 12)
zz = range(0, 31)
jj = range(1, 46)
jj2 = range(51, 52)
nnn = range(1, 999)
c = range(1, 10)

cnp = input("Introduceti CNP: ")
if len(cnp) != 13:
    print("CNP Invalid 1")
    exit()
if int(cnp[7:9]) not in jj and jj2:
    print("CNP Invalid 2")
    exit()


if int(cnp[0]) == 0:
    print("CNP Invalid")
elif int(cnp[0]) == 1:
    print("Sex masculin\nNascut între 1 ianuarie 1900 și 31 decembrie 1999")
elif int(cnp[0]) == 2:
    print("Sex feminin\nNascut între 1 ianuarie 1900 și 31 decembrie 1999")
elif int(cnp[0]) == 3:
    print("Sex masculin\nNascut între 1 ianuarie 1800 și 31 decembrie 1899")
elif int(cnp[0]) == 4:
    print("Sex feminin\nNascut între 1 ianuarie 1800 și 31 decembrie 1899")
elif int(cnp[0]) == 5:
    print("Sex masculin\nNascut între 1 ianuarie 2000 și 31 decembrie 2099")
elif int(cnp[0]) == 6:
    print("Sex feminin\nNascut între 1 ianuarie 2000 și 31 decembrie 2099")
elif int(cnp[0]) == range(7, 8):
    print("Persoana straina\nRezident in Romania")
else:
    print("Persoana straina")
print("Anul este: " + str(cnp[1:3]))
if cnp[3:5] == "01":
    print("Luna este: Ianuarie")
elif cnp[3:5] == "02":
    print("Luna este: Februarie")
elif cnp[3:5] == "03":
    print("Luna este: Martie")
elif cnp[3:5] == "04":
    print("Luna este: Aprilie")
elif cnp[3:5] == "05":
    print("Luna este: Mai")
elif cnp[3:5] == "06":
    print("Luna este: Iunie")
elif cnp[3:5] == "07":
    print("Luna este: Iulie")
elif cnp[3:5] == "08":
    print("Luna este: August")
elif cnp[3:5] == "09":
    print("Luna este: Septembrie")
elif cnp[3:5] == "10":
    print("Luna este: Octombrie")
elif cnp[3:5] == "11":
    print("Luna este: Noiembrie")
elif cnp[3:5] == "12":
    print("Luna este: Decembrie")
print("Ziua este: " + str(cnp[5:7]))
