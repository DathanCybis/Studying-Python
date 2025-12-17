lista = []
class ManipuladorDeLista:
    def __init__(self, elemento):
        self.elemento = elemento


    def adicionar_elemento():
        try:
            num = int(input("Digite um número inteiro para adicionar: "))
        except:
            print("Por favor, digite um número inteiro!")
            return

        lista.append(num)
        print(f"Elemento '{num}' adicionado com sucesso!")


    def remover_elemento():
        try:
            num = int(input("Digite o número inteiro que deseja remover: "))
        except:
            print("Por favor, digite um número inteiro!")
            return

        if num in lista:
            lista.remove(num)
            print(f"Elemento '{num}' removido com sucesso!")
        else:
            print("Por favor, digite um número inteiro válido!")


    def encontrar_maior():
        maior = max(lista)
        print(f"O maior elemento da lista é o: '{maior}'")


    def encontrar_menor():
        menor = min(lista)
        print(f"O menor elemento da lista é o: '{menor}'")


    def calcular_media():
        media = sum((lista)) / len(lista)
        print(f"A média dos elementos da lista é: '{media}'")


    def mostrar_lista():
        print(f"A lista atual é: {lista}")


def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar elemento")
        print("2. Remover elemento")
        print("3. Encontrar maior elemento")
        print("4. Encontrar menor elemento")
        print("5. Calcular média dos elementos")
        print("6. Mostrar lista")
        print("7. Sair")

        opc = input("\nDigite a opção desejada: ")

        if opc == "1":
            ManipuladorDeLista.adicionar_elemento()
        elif opc == "2":
            ManipuladorDeLista.remover_elemento()
        elif opc == "3":
            ManipuladorDeLista.encontrar_maior()
        elif opc == "4":
            ManipuladorDeLista.encontrar_menor()
        elif opc == "5":
            ManipuladorDeLista.calcular_media()
        elif opc == "6":
            ManipuladorDeLista.mostrar_lista()
        elif opc == "7":
            print("Fim do programa...\n")
            break
        else:
            print("Por favor, digite uma opção válida!")

menu()
