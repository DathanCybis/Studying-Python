original = {"a": 1, "b": 2, "c": 3}

invertido = {valor: chave for chave, valor in original.items()}

print(original) # {'a': 1, 'b': 2, 'c': 3}

print(invertido) # {1: 'a', 2: 'b', 3: 'c'}
