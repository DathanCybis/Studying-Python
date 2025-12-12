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
                if self.dirigindo:
                    print(f"{self.nome} não pode comer dirigindo.")
                if not self.acordado:
                    print(f"{self.nome} não pode comer dormindo.")
    

    def parar_de_comer(self):
        if self.comendo:
            self.comendo = False
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
                if self.comendo:
                    print(f"{self.nome} não pode dirigir comendo.")
                if not self.acordado:
                    print(f"{self.nome} não pode dirigir dormindo.")

            
    def parar_de_dirigir(self):
        if self.dirigindo:
            self.dirigindo = False
            print(f"{self.nome} parou de dirigir.")
        else:
            print(f"{self.nome} não está dirigindo.")

    
    def dormir(self):
        if not self.acordado:
            print(f"{self.nome} já está dormindo.")
        else:
            if self.acordado and not self.dirigindo and not self.comendo:
                self.acordado = False
                print(f"{self.nome} começou a dormir.")
            else:
                if self.dirigindo:
                    print(f"{self.nome} não pode dormir enquanto dirige.")
                if self.comendo:
                    print(f"{self.nome} não pode dormir enquanto come.")


joao = Pessoa("João")

joao.acordar() # João acordou.
joao.acordar() # João já está acordado(a).

joao.comer() # João começou a comer.

joao.parar_de_comer() # João parou de comer.
joao.parar_de_comer() # João não está comendo.

joao.dirigir() # João começou a dirigir.
joao.parar_de_dirigir() # João parou de dirigir.

joao.comer() # João começou a comer.

joao.dormir() # João não pode dormir enquanto come.

joao.dirigir() # João não pode dirigir comendo.

joao.parar_de_comer() # João parou de comer.

joao.dormir()

joao.comer()

joao.dormir()

joao.dirigir()
