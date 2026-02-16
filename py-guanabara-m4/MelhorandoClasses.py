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

    
    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"


    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"


g1 = Gafanhoto("Maria", 67)
g1.aniversario()
print(g1)
print(g1.__dict__) # Attribute
print(g1.__getstate__()) # Method
#print(g1.__doc__)
print(g1.__class__)

g2 = Gafanhoto("Mauro", 54)
print(g2)
print(g2.__getstate__())

