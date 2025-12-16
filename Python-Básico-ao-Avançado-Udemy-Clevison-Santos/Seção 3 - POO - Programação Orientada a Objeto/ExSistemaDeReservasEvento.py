class Evento:
    def __init__(self, lugares=10):
        self.lugares = lugares


    def reservar(self):
        if self.lugares > 0:
            self.lugares -= 1
        else:
            print("Não há assentos disponíveis.")


