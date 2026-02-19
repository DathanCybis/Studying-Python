from rich import print
from rich.panel import Panel

print("Olá, [bold red]Mundo[/]! :earth_americas:" )

caixa = Panel("[red]Painel de exemplo[/]", title="Mensagem", width=35)

print(caixa)
