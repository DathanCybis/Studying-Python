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


def analisar(jogador):
    for i in range(3):
        todas_linhas = True
        todas_colunas = True

        for j in range(3):
            if matrix[i][j] != jogador:
                todas_linhas = False

            if matrix[j][i] != jogador:
                todas_colunas = False

    if todas_linhas or todas_colunas:
        return True
    
    if matrix[0][0] == jogador and matrix[1][1] == jogador and matrix[2][2] == jogador:
        return True
    
    if matrix[0][2] == jogador and matrix[1][1] == jogador and matrix[2][0] == jogador:
        return True
     
    return False     


def main():
    cont = 0
    while True:
        mostrar_jogo()
        cont+=1

        if cont % 2 != 0:
            escolha = input("Jogador 'O', escolha a linha e coluna (ex: 0 2): ")
            jogador = "O"
        else:
            escolha = input("Jogador 'X', escolha a linha e coluna (ex: 0 2): ")
            jogador = "X"

        linha = int(escolha[0])
        coluna = int(escolha[2])
        matrix[linha][coluna] = jogador

        if analisar(jogador):
            print(f"Jogador {jogador} venceu!")
            break

        print()


main()
