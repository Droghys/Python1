# dictionarul_meu = {}
# print(type(dictionarul_meu))
dictionarul_meu = {"cheie1": 12, "cheie2": 14, "cheie3": 300, 40: "valoare", 'cheie4': 'valoare noua',
                   'cheie5': 'valoare noua pentru cheia 5'}
# print(dictionarul_meu['cheie2'])
# print(dictionarul_meu.get('cheie4', "Nu exista"))
dictionarul_meu.update({"cheia 4": "vloare noua", "cheie5": "voloare pentru cheia 5"})
print(dictionarul_meu.keys())
print(dictionarul_meu.values())
print(dictionarul_meu.items())
