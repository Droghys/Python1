alegere = int(input("Alegeti un numar: "))

dictionarul_meu = {}
suma = 0

for x in range(1, alegere + 1):
    suma += x  # Adăugăm x la suma valorilor precedente
    dictionarul_meu[x] = suma  # Atribuim suma ca valoare pentru cheia x

print(dictionarul_meu)
