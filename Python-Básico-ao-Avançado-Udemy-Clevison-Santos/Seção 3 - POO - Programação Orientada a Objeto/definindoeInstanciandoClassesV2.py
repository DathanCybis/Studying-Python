class Carro:

    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0


    def acelerar(self):
        self.velocidade += 10
        print(f"Acelerando... Velocidade atual: {self.velocidade} km/h\n")

    
    def frear(self):
        self.velocidade -= 10

        if self.velocidade < 0:
            self.velocidade = 0

        print(f"Freando... Velocidade atual: {self.velocidade} km/h\n")


    def exibir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}\n")


def adicionar_carro():
    marca = input("Marca do carro: ")
    modelo = input("Modelo do carro: ")
    cor = input("Cor do carro: ")

    return Carro(marca, modelo, cor)


def main():
    lista = []

    while True:
        print(" --- MENU --- ")
        print("1. Adicionar novo carro")
        print("2. Exibir informações dos carros")
        print("3. Acelerar um carro")
        print("4. Frear um carro")
        print("5. Sair")

        opc = input("\nDigite a opção desejada: ")

        if opc == "1":
            carro = adicionar_carro()
            print("\nCarro adicionado com sucesso!\n")
        elif opc == "2":
            carro.exibir_info()
        elif opc == "3":
            carro.acelerar()
        elif opc == "4":
            carro.frear()
        elif opc == "5":
            print("\nFinalizando o sistema...")
            break
        else:
            print("Digite uma opção válida!\n")


main()
