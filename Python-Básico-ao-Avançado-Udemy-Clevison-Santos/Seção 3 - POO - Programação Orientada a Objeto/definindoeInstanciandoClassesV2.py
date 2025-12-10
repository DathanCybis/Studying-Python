class Carro:

    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0


    def acelerar(self):
        self.velocidade += 10
        print(f"Acelerando {self.modelo}... Velocidade atual: {self.velocidade} km/h\n")

    
    def frear(self):
        self.velocidade -= 10

        if self.velocidade < 0:
            self.velocidade = 0

        print(f"Freando... Velocidade atual: {self.velocidade} km/h\n")


    def exibir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}, Velocidade: {self.velocidade} km/h")


def adicionar_carro():
    marca = input("Marca do carro: ")
    modelo = input("Modelo do carro: ")
    cor = input("Cor do carro: ")

    return Carro(marca, modelo, cor)


def main():
    lista_carros = []

    while True:
        print("\n --- MENU --- ")
        print("1. Adicionar novo carro")
        print("2. Exibir informações dos carros")
        print("3. Acelerar um carro")
        print("4. Frear um carro")
        print("5. Sair")

        opc = input("\nDigite a opção desejada: ")

        if opc == "1":
            novo_carro = adicionar_carro()
            lista_carros.append(novo_carro)
            print("\nCarro adicionado com sucesso!")

        elif opc == "2":
            if lista_carros:
                for carro in lista_carros:
                    carro.exibir_info()
            else:
                print("\nNenhum carro foi adicionado ainda.")

        elif opc == "3":
            modelo = input("\nDigite o modelo do carro que quer acelerar: ")

            for carro in lista_carros:
                if carro.modelo == modelo:
                    carro.acelerar()
                    break
            else:
                print("Modelo não encontrado.")

        elif opc == "4":
            modelo = input("\nDigite o modelo do carro que quer frear: ")

            for carro in lista_carros:
                if carro.modelo == modelo:
                    carro.frear()
                    break
            else:
                print("Modelo não encontrado.")

        elif opc == "5":
            print("\nFinalizando o sistema...\n")
            break

        else:
            print("Digite uma opção válida!")


main()
