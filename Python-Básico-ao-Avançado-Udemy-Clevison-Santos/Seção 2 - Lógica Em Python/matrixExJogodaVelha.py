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
 

def verificar_ganhador(jogador):
    for linha in range(3):
        total_coluna = True
        total_linha = True
        for coluna in range(3):
            if matrix[coluna][linha] != jogador:
                total_coluna = False
            if matrix[linha][coluna] != jogador:
                total_linha = False
        if total_coluna or total_linha:
            return True
    if matrix[0][0] == jogador and matrix[1][1] == jogador and matrix[2][2] == jogador:
        return True
    if matrix[0][2] == jogador and matrix[1][1] == jogador and matrix[2][0] == jogador:
        return True
    
    return False


def main():
    cont = 0
    for _ in range(9):
        mostrar_jogo()

        if cont % 2 != 0:
            escolha = input("Jogador 'O', escolha a linha e coluna (ex: 0 2): ")
            jogador = "O"
        else:
            escolha = input("Jogador 'X', escolha a linha e coluna (ex: 0 2): ")
            jogador = "X"

        linha = int(escolha[0])
        coluna = int(escolha[2])
        if matrix[linha][coluna] == "°":
            matrix[linha][coluna] = jogador
            cont+=1
        else:
            print("Posição já ocupada, tente novamente!")

        if verificar_ganhador(jogador):
            mostrar_jogo()
            print(f"Fim do jogo! O jogador '{jogador}' venceu!")
            break
        print()
    else:
        mostrar_jogo()
        print("Fim do jogo! Empate, deu velha!!")


main()
