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


    def exibir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}")


carro1 = Carro("Toyota", "Corolla", "Preto")

carro1.exibir_info() # Marca: Toyota, Modelo: Corolla, Cor: Preto
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
carro1.acelerar()
