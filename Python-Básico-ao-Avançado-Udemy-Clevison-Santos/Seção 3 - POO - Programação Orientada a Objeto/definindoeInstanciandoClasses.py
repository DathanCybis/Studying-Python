class Carro:

    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0


    def acelerar(self):
        self.velocidade += 10
        print(f"Acelerando... Velocidade atual: {self.velocidade} km/h")

    
    def frear(self):
        self.velocidade -= 10

        if self.velocidade < 0:
            self.velocidade = 0

        print(f"Freando... Velocidade atual: {self.velocidade} km/h")


    def exibir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}")


carro1 = Carro("Toyota", "Corolla", "Preto")

carro1.exibir_info() # Marca: Toyota, Modelo: Corolla, Cor: Preto
carro1.acelerar() # Acelerando... Velocidade atual: 10 km/h
carro1.acelerar() # Acelerando... Velocidade atual: 20 km/h
carro1.acelerar() # Acelerando... Velocidade atual: 30 km/h
carro1.acelerar() # Acelerando... Velocidade atual: 40 km/h
carro1.frear() # Freando... Velocidade atual: 30 km/h
carro1.frear() # Freando... Velocidade atual: 20 km/h

print()
print()

carro2 = Carro("Ford", "Fiesta", "Prata")
carro2.exibir_info() # Marca: Ford, Modelo: Fiesta, Cor: Prata
carro2.acelerar() # Acelerando... Velocidade atual: 10 km/h
carro2.acelerar() # Acelerando... Velocidade atual: 20 km/h
carro2.frear() # Freando... Velocidade atual: 10 km/h
