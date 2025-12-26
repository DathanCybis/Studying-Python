class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


    def exibir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor


    def exibir_info(self):
        super().exibir_info()
        print(f"Cor: {self.cor}")


veiculo = Veiculo("Honda", "Civic")

veiculo.exibir_info() # Marca: Honda, Modelo: Civic

carro = Carro("Toyota", "Corolla", "Chumbo")

carro.exibir_info() # Marca: Toyota, Modelo: Corolla \n Cor: Chumbo
