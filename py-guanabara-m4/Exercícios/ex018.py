from rich import print

class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant


c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()
