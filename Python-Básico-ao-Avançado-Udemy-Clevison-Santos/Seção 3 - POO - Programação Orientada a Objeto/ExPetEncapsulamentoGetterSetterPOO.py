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



def main():
    meu_pet = Pet()
    while True:
        print("\n1. Definir nome do pet")
        print("2. Definir idade do pet")
        print("3. Definir peso do pet")
        print("4. Exibir informações do pet")
        print("5. Sair")



