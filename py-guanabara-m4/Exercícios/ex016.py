from rich import print
from rich import inspect

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def apresentacao(self):
        return f":wave: Olá, sou [bold blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor}, da empresa Curso em Vídeo"


c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentacao())
inspect(c1)

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentacao())
inspect(c2)

c3 = Funcionario("João", "Administração", "Contador")
print(c3.apresentacao())
inspect(c3)
