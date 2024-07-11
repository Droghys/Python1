operatii_matematice = '+-*/'
operator_1 = input("Primul operator: ")
# operator_2 = input("Al doilea operator: ")
# verificam daca ceea ce introduce utilizatorul este in intervalul 0-9 sau contine .
stare_conversie = True
for element in operator_1:
    if element not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        stare_conversie = False
        break
print(stare_conversie, 'stare conversie')
