from rich import print
from rich.panel import Panel

class Churrasco:

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/green] com [blue]{self.quant} convidados[/blue]"
        conteudo += f"\nCada participante comerá 0.4kg e cada Kg custa R$82.40"
        totalkg = (0.4 * self.quant)
        carne =  totalkg * 82.4
        conteudo += f"\nRecomendo [blue]comprar {totalkg:.3f}kg[/blue] de carne"
        conteudo += f"\nO custo total será de [green]R${carne:.2f}[/green]"
        precoporpessoa = carne / self.quant
        conteudo += f"\nCada pessoa pagará [green]R${precoporpessoa:.2f}[/green] para participar."
        a = Panel(conteudo, title=self.titulo)
        print(a)

c1 = Churrasco("Churras dos Amigos", 56)
c1.analisar()