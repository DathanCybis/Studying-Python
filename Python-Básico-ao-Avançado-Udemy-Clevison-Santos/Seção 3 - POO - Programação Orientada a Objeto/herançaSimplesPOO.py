class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def exibir_info(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}")


    