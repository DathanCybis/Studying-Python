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

    
meu_pet = Pet()
meu_pet.set_nome("Bob")
meu_pet.set_idade(2)
meu_pet.set_peso(4)
meu_pet.exibir_infos()

print("\n -------------- \n")

meu_pet.set_nome("Lua")
meu_pet.set_idade(4)
meu_pet.set_peso(8.3)
meu_pet.exibir_infos()

print("\n -------------- \n")

meu_pet.set_nome("Jaspion")
meu_pet.set_idade(8)
meu_pet.set_peso(9.3)
meu_pet.exibir_infos()
