class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.acordado = False
        self.comendo = False
        self.dirigindo = False


    def acordar(self):
        if self.acordado:
            print(f"{self.nome} já está acordado(a).")
        else:
            self.acordado = True
            print(f"{self.nome} acordou.")
    
    
