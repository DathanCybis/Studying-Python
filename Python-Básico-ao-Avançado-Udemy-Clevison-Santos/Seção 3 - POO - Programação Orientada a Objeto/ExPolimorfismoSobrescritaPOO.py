class Veiculo():
    def mover(self):
        print("O veículo está se movendo")


class Carro(Veiculo):
    def mover(self):
        print("O carro está se movendo na estrada")


class Barco(Veiculo):
    def mover(self):
        print("O barco está se movendo na água")


class Aviao(Veiculo):
    def mover(self):
        print("O avião está se movendo no céu")


veiculo = Veiculo()

carro = Carro()

barco = Barco()

aviao = Aviao()


veiculo.mover() # O veículo está se movendo

carro.mover() # O carro está se movendo na estrada

barco.mover() # O barco está se movendo na água

aviao.mover() # O avião está se movendo no céu
