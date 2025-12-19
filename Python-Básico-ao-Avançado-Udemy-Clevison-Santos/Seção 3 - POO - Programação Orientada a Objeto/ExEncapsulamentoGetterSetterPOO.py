class Pet:
    def __init__(self):
        self._nome = ""
        self._idade = 0
        self._peso = 0.0


    def set_nome(self, nome):
        try:
            str(nome)
            if nome.isalpha():
                self._nome = nome
            else:
                print("O nome deve ser uma string e não vazio")
        except:
            print("O nome deve ser uma string e não vazio!")
        
    
    def set_idade(self, idade):
        if idade == int(idade) and idade >= 0:
            self._idade = idade
        else:
            print("A idade deve ser um número inteiro e maior ou igual a 0")


    def set_peso(self, peso):
        peso = float(peso)
        if peso >= 0:
            self._peso = peso
        else:
            print("O peso deve ser flutuante e maior ou igual a 0")


    def exibir_infos(self):
        print(f"O nome do pet é {self._nome}")
        print(f"A idade do pet é {self._idade}")
        print(f"O peso do pet é {self._peso}")

    
meu_pet = Pet()
meu_pet.set_nome("")
meu_pet.set_idade(2)
meu_pet.set_peso(4)
meu_pet.exibir_infos()
