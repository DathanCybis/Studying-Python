class ManipuladorDeLista:
    def __init__(self):
        self.lista = []


    def adicionar_elemento(self):
        try:
            num = int(input("Digite um número inteiro para adicionar: "))
        except:
            print("Por favor, digite um número inteiro!")
            return

        self.lista.append(num)
        print(f"Elemento '{num}' adicionado com sucesso!")


    def remover_elemento(self):
        try:
            num = int(input("Digite o número inteiro que deseja remover: "))
        except:
            print("Por favor, digite um número inteiro!")
            return

        if num in self.lista:
            self.lista.remove(num)
            print(f"Elemento '{num}' removido com sucesso!")
        else:
            print("Por favor, digite um número inteiro válido!")


    def encontrar_maior(self):
        if self.lista:
            maior = max(self.lista)
            print(f"O maior elemento da lista é o: '{maior}'")
        else:
            print("A lista está vazia.")


    def encontrar_menor(self):
        if self.lista:
            menor = min(self.lista)
            print(f"O menor elemento da lista é o: '{menor}'")
        else:
            print("A lista está vazia.")


    def calcular_media(self):
        if self.lista:
            media = sum((self.lista)) / len(self.lista)
            print(f"A média dos elementos da lista é: '{media}'")
        else:
            print("A lista está vazia.")


    def mostrar_lista(self):
        print(f"A lista atual é: {self.lista}")


def menu():
    manipulador = ManipuladorDeLista()
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
            manipulador.adicionar_elemento()
        elif opc == "2":
            manipulador.remover_elemento()
        elif opc == "3":
            manipulador.encontrar_maior()
        elif opc == "4":
            manipulador.encontrar_menor()
        elif opc == "5":
            manipulador.calcular_media()
        elif opc == "6":
            manipulador.mostrar_lista()
        elif opc == "7":
            print("Fim do programa...\n")
            break
        else:
            print("Por favor, digite uma opção válida!")


if __name__ == "__main__":
    menu()
