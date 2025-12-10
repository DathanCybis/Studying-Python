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


def adicionar_carro():
    pass


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
            adicionar_carro()
        elif opc == "2":
            Carro.exibir_info()
        elif opc == "3":
            pass
        elif opc == "4":
            pass
        elif opc == "5":
            pass
        else:
            print("Digite uma opção válida!\n")


main()
