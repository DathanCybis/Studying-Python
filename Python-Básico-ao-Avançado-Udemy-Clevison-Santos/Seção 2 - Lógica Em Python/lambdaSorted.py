pessoas = [("João", 25), ("Maria", 35), ("Pedro", 30)]

pessoas_sorted = sorted(pessoas, key=lambda x: x[1])
 
print(pessoas_sorted) # Saída: [('João', 25), ('Pedro', 30), ('Maria', 35)]
