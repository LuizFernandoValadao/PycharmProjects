from rich import print
from rich.panel import Panel
import time
from rich.progress import track

caixa = Panel("[blue]Esse aqui é um painel de exemplo[/blue]", title="Mensagem", style="red")
print(caixa)

caixa = Panel.fit("[blue]Esse aqui é um painel de exemplo[/blue]", title="Mensagem", style="red")
print(caixa)

caixa = Panel("[blue]Esse aqui é um painel de exemplo[/blue]", title="Mensagem", style="red", subtitle="Exemplo")
print(caixa)

for i in track(range(20), description="Processing..."):
    time.sleep(1)  # Simulate work being done