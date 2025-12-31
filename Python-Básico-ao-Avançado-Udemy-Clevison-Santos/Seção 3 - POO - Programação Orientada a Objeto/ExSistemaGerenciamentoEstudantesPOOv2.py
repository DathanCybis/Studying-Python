alunos = []
class Estudante:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota


    def get_nome(self):
        return self.nome

    
    def get_idade(self):
        return self.idade
    

    def get_nota(self):
        return self.nota
    

    def set_nome(self, nome):
        self.nome = nome

    
    def set_idade(self, idade):
        self.idade = idade
    

    def set_nota(self, nota):
        self.nota = nota
    

    
