class Pet:
    def __init__(self):
        self._nome = ""
        self._idade = 0
        self._peso = 0.0


    def get_nome(self):
        return self._nome


    def get_idade(self):
        return self._idade


    def get_peso(self):
        return self._peso
        

    def set_nome(self, nome):
        if isinstance(nome, str) and nome != "":
            self._nome = nome
        else:
            print("O nome deve ser uma string e não vazio")

        
    
    def set_idade(self, idade):
        if idade == int(idade) and idade >= 0:
            self._idade = idade
        else:
            print("A idade deve ser um número inteiro e maior ou igual a 0")


    def set_peso(self, peso):
        peso = float(peso)
        if peso > 0:
            self._peso = peso
        else:
            print("O peso deve ser flutuante e maior que 0")


    def exibir_infos(self):
        print(f"Nome: {self._nome}")
        print(f"Idade: {self._idade}")
        print(f"Peso: {self._peso} kg")


def mostrar_menu():
    print("\n1. Definir nome do pet")
    print("2. Definir idade do pet")
    print("3. Definir peso do pet")
    print("4. Exibir informações do pet")
    print("5. Sair")

    opc = input("\nDigite a opção desejada: ")

    return opc


def main():
    meu_pet = Pet()
    while True:
        opc = mostrar_menu()

        if opc == "1":
            nome = input("Nome: ")
            meu_pet.set_nome(nome)

        elif opc == "2":
            try:
                idade = int(input("Idade: "))
                meu_pet.set_idade(idade)
            except ValueError:
                print("Idade inválida, por favor insira um número inteiro.")

        elif opc == "3":
            try:
                peso = input("Peso: ")
                meu_pet.set_peso(peso)
            except ValueError:
                print("Peso inválido, por favor insira um número positivo.")

        elif opc == "4":
            meu_pet.exibir_infos()
        elif opc == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")


main()
