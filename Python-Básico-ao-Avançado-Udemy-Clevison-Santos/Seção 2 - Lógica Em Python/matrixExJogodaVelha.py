matrix = [
    ["°", "°", "°"],
    ["°", "°", "°"],
    ["°", "°", "°"]
]

def mostrar_jogo():
    for linha in matrix:
        print(" ---" * 3)
        print("|", end=" ")
        for coluna in linha:
            print(f"{coluna} |", end=" ")
        print()
        print(" ---" * 3)
    print()
 

def main():
    cont = 0
    while True:
        cont+=1
        mostrar_jogo()

        if cont % 2 != 0:
            escolha = input("Jogador 'O', escolha a linha e coluna (ex: 0 2): ")
            jogador = "O"
        else:
            escolha = input("Jogador 'X', escolha a linha e coluna (ex: 0 2): ")
            jogador = "X"

        linha = int(escolha[0])
        coluna = int(escolha[2])
        matrix[linha][coluna] = jogador

        print()


main()
