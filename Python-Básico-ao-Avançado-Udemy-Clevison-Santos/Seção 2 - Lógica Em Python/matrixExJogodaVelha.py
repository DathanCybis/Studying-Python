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
            pass

main()