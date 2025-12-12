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
    
    
    def comer(self):
        if self.comendo:
            print(f"{self.nome} já está comendo.")
        else:
            if not self.dirigindo or self.acordado: 
                self.comendo = True
                print(f"{self.nome} começou a comer.")
    
