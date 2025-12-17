lista = [10, 5]
class ManipuladorDeLista:
    def __init__(self, elemento):
        self.elemento = elemento


    def adicionar_elemento():
        num = input("Digite um número inteiro para adicionar: ")

        if num == int:
            lista.append(int(num))
        else:
            print("Por favor, digite um número inteiro!")


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



ManipuladorDeLista.encontrar_maior()
ManipuladorDeLista.encontrar_menor()
ManipuladorDeLista.calcular_media()
ManipuladorDeLista.mostrar_lista()
