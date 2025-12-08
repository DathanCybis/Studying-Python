matrix = [
    ["°", "°", "°"],
    ["°", "O", "°"],
    ["°", "O", "°"]
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
    total_linha = 0
    for linha in matrix:
        if total_linha == 3:
            return True
        total_linha = 0
        for coluna in linha:
            if coluna == jogador:
                total_linha+=1

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

    return False


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
        if verificar_ganhador(jogador):
            mostrar_jogo()
            print(f"Fim do jogo! O jogador '{jogador}' venceu!")
            break
        print()


main()
