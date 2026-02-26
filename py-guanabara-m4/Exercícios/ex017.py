from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def etiqueta(self):
        conteudo = f"{self.nome.center(51, ' ')}"
        conteudo += f"{'-' * 51}"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(51, '.')}"

        etqNome = Panel(f"{conteudo}", title="Produto", width=55)
        print(etqNome)


p1 = Produto("iPhone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8_000)

p1.etiqueta()
p2.etiqueta()
