class Termometro:
    def __init__(self):
        pass


    @property
    def temperatura(self):
        return self._temperatura
    

    @temperatura.setter
    def temperatura(self, valor):
        if valor > -100 and valor < 100:
            self._temperatura = valor
        else:
            print("Certifique-se que a temperatura esteja entre -100 e 100")


t = Termometro()

t.temperatura = 25

print(t.temperatura) # 25

t.temperatura = 250 # Certifique-se que a temperatura esteja entre -100 e 100

t.temperatura = 27

print(t.temperatura) # 27
