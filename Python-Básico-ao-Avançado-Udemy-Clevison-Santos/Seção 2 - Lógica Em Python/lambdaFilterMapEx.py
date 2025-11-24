numeros = [2, 5, 8, 10, 12, 15, 18, 20, 23, 25, 28]

impares = list(filter(lambda x: x % 2 != 0, numeros))

print(impares) # Saída: [5, 15, 23, 25]

impares_ao_quadrado = list(map(lambda x: x**2, impares))

print(impares_ao_quadrado) # Saída: [25, 225, 529, 625]
