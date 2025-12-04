urna = [["Alice", 0], ["Bob", 0], ["Charlie", 0]]

for n in range(4):
    voto = input("Digite o nome de quem quer votar (Alice, Bob ou Charlie): ")

    encontrado = False

    for candidato in urna:
        if candidato[0] == voto:
            candidato[1] += 1
            encontrado = True
            break
    
    if not encontrado:
        print("Voto nulo!")

print("\nResultados:")

maior = 0
vencedor = ""

for candidato in urna:
    print(f"{candidato[0]}: {candidato[1]}")

    if candidato[1] > maior:
        maior = candidato[1]
        vencedor = candidato[0]

print(f"O vencedor é {vencedor} com {maior} votos")
