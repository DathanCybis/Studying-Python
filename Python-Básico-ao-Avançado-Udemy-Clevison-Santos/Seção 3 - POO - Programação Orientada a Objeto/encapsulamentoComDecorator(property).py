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
    


