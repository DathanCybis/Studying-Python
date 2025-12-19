class Pet:
    def __init__(self, nome, idade, peso):
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
        print(f"O nome do pet é {nome}")
    

    def set_idade(self, idade):
        print(f"A idade do pet é {idade}")


    def set_peso(self, peso):
        print(f"O peso do pet é {peso}")

    