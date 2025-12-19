class Pet:
    def __init__(self, nome=None, idade=None, peso=None):
        self._nome = nome
        self._idade = idade
        self._peso = peso


    def get_nome(self):
        return self._nome
    

    def get_idade(self):
        return self._idade


    def get_peso(self):
        return self._peso
    

    def set_nome(self, nome):
        try:
            if nome == str(nome):
                self._nome = nome
        except:
            print("O nome deve ser uma string e não vazio")
        
    
    def set_idade(self, idade):
        self._idade = idade


    def set_peso(self, peso):
        self._peso = peso


    def exibir_infos(self):
        print(f"O nome do pet é {self._nome}")
        print(f"A idade do pet é {self._idade}")
        print(f"O peso do pet é {self._peso}")

    
meu_pet = Pet()
meu_pet.set_nome("")
meu_pet.set_idade(2)
meu_pet.set_peso(4)
meu_pet.exibir_infos()
