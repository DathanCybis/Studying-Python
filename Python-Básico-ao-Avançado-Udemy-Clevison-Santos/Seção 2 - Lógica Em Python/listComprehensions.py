quadrado = [x**2 for x in range(0, 10)]
quadrado_par = [x**2 for x in range(0, 10) if x % 2 == 0]

print(quadrado) # Saída: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(quadrado_par)# Saída: [0, 4, 16, 36, 64]
