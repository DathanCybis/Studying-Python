from rich import print
from rich.panel import Panel
from rich.table import Table

print("Olá, [bold red]Mundo[/]! :earth_americas:" )

caixa = Panel("[red]Painel de exemplo[/]", title="Mensagem", width=35)

print(caixa)

tabela = Table(title="Tabela de preços")

tabela.add_column("Nome")
tabela.add_column("Preço")
tabela.add_row("Lápis", "R$1.50")
tabela.add_row("Borracha", "R$5.60")

print(tabela)
