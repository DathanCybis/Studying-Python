class Evento:
    def __init__(self, lugares=10):
        self.lugares = lugares


    def reservar(self):
        if self.lugares > 0:
            self.lugares -= 1
        else:
            print("Não há assentos disponíveis.")


    def cancelar(self):
        if self.lugares < 10:
            self.lugares += 1
        else:
            print("Não há nenhuma reserva para cancelar.")


def main():
    while True:
        print("Sistema de reservas para um evento")
        print("1. Reservar")
        print("2. Cancelar")

        opc = input("Digite a opção que deseja: ")

        if opc == "1":
            pass
        elif opc == "2":
            pass
        else:
            print("Digite uma opção válida!")