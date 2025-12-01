conjunto = {1, 2, "Python", (4, 5)}

print(conjunto) # {'Python', 1, 2, (4, 5)}
# Ordem aleatória

try:
    conjunto.add([6,7])
except TypeError as e:
    print(f"Erro: {e}") # Erro: unhashable type: 'list'
# Isso acontece porque os elementos dentro de um conjunto(sets) são imutáveis
