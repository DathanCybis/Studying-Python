quadrados_impares = [x**2 for x in range(1, 10) if x % 2 != 0]
print(quadrados_impares)

# OR

quadrados_impares2 = []
for x in range(1, 10):
    if x % 2 != 0:
        x = x**2
        quadrados_impares2.append(x)

print(quadrados_impares2)
