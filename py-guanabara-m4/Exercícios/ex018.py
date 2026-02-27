from rich import print

class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant


    def analisar(self):
        por_participante = 0.4
        kg_preco = 82.40
        recomendado = 6.0
        print(f"Analisando [red]{self.titulo}[/] com [blue]{self.quant} convidados[/]")
        print(f"Cada participante comerá [yellow]{por_participante}Kg[/] e cada Kg custa [green]R${kg_preco:.2f}[/]")
        print(f"Recomendo comprar [yellow]{recomendado:.3f}Kg[/] de carne")
        custo_total = por_participante * self.quant
        custo_total *= kg_preco
        
        print(f"O custo total será de [green]R${custo_total:.2f}[/]")
        cada_pessoa = custo_total / self.quant
        print(f"Cada pessoa pagará [green]R${cada_pessoa}[/] para participar.")
        


c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()
