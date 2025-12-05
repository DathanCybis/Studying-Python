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


def main():
    while True:
        mostrar_menu()