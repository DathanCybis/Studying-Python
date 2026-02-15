class Gafanhoto:
    """
    Docstring for Gafanhoto:
    Essa classe cria um Gafanhoto
    """
    def __init__(self, nome = "", idade= 0):
        self.nome = nome
        self.idade = idade


    def aniversario(self):
        self.idade += 1

    
    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"
    

g1 = Gafanhoto("Maria", 67)
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto("Mauro", 53)
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())

print(g1.__doc__)
