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

        if cont % 2 != 0:
            escolha = int(input("Jogador 'O', escolha a linha e coluna (ex: 1 3): "))
        else:
            escolha = int(input("Jogador 'X', escolha a linha e coluna (ex: 1 3): "))
        
        

main()