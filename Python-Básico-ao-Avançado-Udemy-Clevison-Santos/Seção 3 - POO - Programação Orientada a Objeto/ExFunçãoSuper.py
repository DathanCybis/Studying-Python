class Veiculo:
    def exibir_info(self):
        print(f"Marca: Ferrari")


class Carro(Veiculo):
    def exibir_info(self):
        super().exibir_info()
        print(f"Cor: Vermelho")


veiculo = Veiculo()

veiculo.exibir_info() # Marca: Ferrari

carro = Carro()

carro.exibir_info() # Marca: Ferrari \n Cor: Vermelho
