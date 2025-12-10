class Carro:

    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0


    def acelerar(self):
        self.velocidade += 10
        print(f"Acelerando... Velocidade atual: {self.velocidade} km/h")

    
    def freiar(self):
        self.velocidade -= 10
        print(f"Freiando... Velocidade atual: {self.velocidade} km/h")


    