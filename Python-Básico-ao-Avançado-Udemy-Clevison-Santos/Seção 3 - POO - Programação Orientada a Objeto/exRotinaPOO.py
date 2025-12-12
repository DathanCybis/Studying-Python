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
            if not self.dirigindo and self.acordado: 
                self.comendo = True
                print(f"{self.nome} começou a comer.")
            else:
                print(f"{self.nome} não pode comer dirigindo ou dormindo.")
    

    def parar_de_comer(self):
        if self.comendo:
            print(f"{self.nome} parou de comer.")
        else:
            print(f"{self.nome} não está comendo.")

    
    def dirigir(self):
        if self.dirigindo:
            print(f"{self.nome} já está dirigindo.")
        else:
            if not self.comendo and self.acordado:
                self.dirigindo = True
                print(f"{self.nome} começou a dirigir.")
            else:
                print(f"{self.nome} não pode dirigir comendo ou dormindo.")

            
    def parar_de_dirigir(self):
        if self.dirigindo:
            self.dirigindo = False
            print(f"{self.nome} parou de dirigir.")
        else:
            print(f"{self.nome} não está dirigindo.")

    
    