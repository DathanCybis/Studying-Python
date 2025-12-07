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
        mostrar_jogo()
        cont+=1

        if cont % 2 != 0:
            escolha = input("Jogador 'O', escolha a linha e coluna (ex: 0 2): ")
            jogada = "O"
        else:
            escolha = input("Jogador 'X', escolha a linha e coluna (ex: 0 2): ")
            jogada = "X"

        linha = int(escolha[0])
        coluna = int(escolha[2])
        matrix[linha][coluna] = jogada
        
        print()
        

main()
