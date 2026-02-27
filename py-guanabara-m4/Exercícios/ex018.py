from rich import print

class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant


    def analisar(self):
        por_participante = 0.4
        kg_preco = 82.40
        recomendado = 6.0

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()
