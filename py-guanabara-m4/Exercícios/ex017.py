from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def etiqueta(self):
        etqNome = Panel(f"{self.nome} \n R${self.preco:,.2f}", title="Produto", width=55)
        print(etqNome)


p1 = Produto("iPhone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8_000)

p1.etiqueta()
p2.etiqueta()
