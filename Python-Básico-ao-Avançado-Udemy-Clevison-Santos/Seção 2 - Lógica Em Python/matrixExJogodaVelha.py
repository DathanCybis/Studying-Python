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


def aplicar_escolha(escolha):
    matrix[escolha[0]][escolha[2]] = ""


def main():
    cont = 0
    while True:
        mostrar_jogo()
        cont+=1

        if cont % 2 != 0:
            escolha = input("Jogador 'O', escolha a linha e coluna (ex: 1 3): ")
            matrix[escolha[0]][escolha[2]] = "O"
        else:
            escolha = input("Jogador 'X', escolha a linha e coluna (ex: 1 3): ")
            matrix[escolha[0]][escolha[2]] = "X"
        
        aplicar_escolha(escolha)

        print(escolha)
        print()
        

main()