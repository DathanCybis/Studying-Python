class Mamifero:
    def __init__(self):
        print("Sou um mamifero...")


    def amamentar(self):
        print("Amamentando...")


class Ave:
    def __init__(self):
        print("Sou uma ave...")


    def voar(self):
        print("Voando...")


class Morcego(Mamifero, Ave):
    def __init__(self):
        Mamifero.__init__(self)
        Ave.__init__(self)

        print("Sou um morcego...")


    def emitir_som(self):
        print("Emitindo som de ecolocalização...")


morcego = Morcego() # Sou um mamifero... \n # Sou uma ave... \n # Sou um morcego...

morcego.amamentar() # Amamentando...

morcego.voar() # Voando...

morcego.emitir_som() # Emitindo som de ecolocalização...
