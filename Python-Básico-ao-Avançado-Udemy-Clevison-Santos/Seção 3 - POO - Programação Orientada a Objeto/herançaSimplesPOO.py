class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def exibir_info(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}")


class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):

        Pessoa.__init__(nome, idade)
        self.matricula = matricula

    
    def estudar(self):
        print(f"{self.nome} está estudando)")


    