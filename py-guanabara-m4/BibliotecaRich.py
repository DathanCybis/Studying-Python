from rich import print
from rich.panel import Panel
from rich.table import Table

print("Olá, [bold red]Mundo[/]! :earth_americas:" )

caixa = Panel("[red]Painel de exemplo[/]", title="Mensagem", width=35)

print(caixa)

tabela = Table(title="Tabela de preços")

tabela.add_column("Nome")
tabela.add_column("Preço")

print(tabela)
