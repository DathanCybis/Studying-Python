class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def exibir_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")


class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):

        Pessoa.__init__(self, nome, idade)
        self.matricula = matricula

    
    def estudar(self):
        print(f"{self.nome} está estudando.")


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):

        Pessoa.__init__(self, nome, idade)
        self.disciplina = disciplina


    def ensinando(self):
        print(f"{self.nome} está ensinando {self.disciplina}")


pessoa = Pessoa("Maria", 40)

estudante = Estudante("João", 18, "12345")

professor = Professor("Carlos", 50, "Matemática")

pessoa.exibir_info() # Nome: Maria, Idade: 40
estudante.exibir_info() # Nome: João, Idade: 18
estudante.estudar() # João está estudando.

