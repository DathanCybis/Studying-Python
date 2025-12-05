matrix = [
    ["D", "D"]*5,
    ["D", "D"]*5,
    ["D", "D"]*5,
    ["D", "D"]*5
]

def mostrar_matrix():
    for linha in matrix:

        for coluna in linha:

            print(coluna, end=" ")

        print()


def mostrar_menu():
    print("\nMenu:")
    print("1. Ver disposição dos assentos")
    print("2. Reservar um assento")
    print("3. Sair")


def reservar_assento():
    fileira = int(input("Digite o número da fileira / Linha (1-4): "))-1
    


def main():
    while True:
        mostrar_menu()

        opc = input("\nEscolha a opção desejada: ")

        if opc == "1":
            mostrar_matrix()
        elif opc == "2":
            reservar_assento()
        elif opc == "3":
            print("\nSaindo...")
            break
        else:
            print("Digite uma opção válida!")

main()
