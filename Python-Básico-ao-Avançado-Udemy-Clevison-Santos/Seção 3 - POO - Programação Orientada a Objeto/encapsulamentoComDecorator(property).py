class Retangulo:
    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura


    @property
    def largura(self):
        return self._largura
    

    @largura.setter
    def largura(self, valor):
        if valor > 0:
            self._largura = valor
        else:
            print("Largura deve ser maior que 0")


    @property
    def altura(self):
        return self._altura
    

    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self._altura = valor
        else:
            print("Altura deve ser maior que 0")

    @property
    def area(self):
        return self._largura * self._altura
    

r = Retangulo(5, 6)

print("Área:", r.area) # Área: 30

r.largura = 7

print("Nova Área:", r.area) # Nova Área: 42

r.largura = -5 # Largura deve ser maior que 0
