urna = [["Alice", 0], ["Bob", 0], ["Charlie", 0]]

for n in range(4):
    voto = input("Digite o nome de quem quer votar (Alice, Bob ou Charlie): ")

    if "Alice" in voto:
        urna[0][1] += 1
    elif "Bob" in voto:
        urna[1][1] += 1
    elif "Charlie" in voto:
        urna[2][1] += 1
    else:
        print("Candidato não existe!")

print(urna)
