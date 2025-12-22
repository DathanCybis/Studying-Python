class Termometro:
    def __init__(self, temperatura):
        self._temperatura = temperatura

    @property
    def temperatura(self):
        return self._temperatura
    

    @temperatura.setter
    def temperatura(self, valor):
        if valor > -100 and valor < 100:
            self._temperatura = valor
        else:
            print("Certifique-se que a temperatura esteja entre -100 e 100")


