nomes = ["Alice", "Bob", "Anna", "Charlie", "Alex", "Wendel", "Tom"]

nomes_com_A = list(filter(lambda x: x[0] == "A", nomes))

print(nomes_com_A) # Saída: ['Alice', 'Anna', 'Alex']
