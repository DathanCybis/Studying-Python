soma = 0

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[1][2]) # Saída: 6

for linha in matriz:

    for numero in linha:

        soma += numero

print("\n", soma) # Saída: 45
