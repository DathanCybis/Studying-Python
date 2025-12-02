s = {1, 2, 3, 4}
print(s) # {1, 2, 3, 4}

s.add(5)
print(s) # {1, 2, 3, 4, 5}

s.remove(5) # Gera erros se não houver o número a ser excluído
print(s) # {1, 2, 3, 4}

s.discard(4) # Não gera erros se não houver o número a ser excluído
print(s) # {1, 2, 3}

elemento_removido = s.pop()
print(elemento_removido) # 1
print(s) # {2, 3}

s.clear()
print(s) # set()
