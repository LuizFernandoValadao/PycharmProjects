from rich import print
from rich.panel import Panel
from poligono import *

def main():
    q1 = Quadrado()
    conteudo = f"[blue]Perímetro [/]= [green]{q1.perímetro():.1f}[/]"
    conteudo += f"\n[blue]Area [/]= [green]{q1.area():.1f}[/]"
    panel = Panel.fit(conteudo, title='< DADOS QUADRADO>', style='cyan')
    print(panel)

    c1 = Círculo(20)
    conteudo = f"[blue]Perímetro [/]= [green]{c1.perímetro():.1f}[/]"
    conteudo += f"\n[blue]Area [/]= [green]{c1.area():.1f}[/]"
    panel = Panel.fit(conteudo, title='< DADOS CÍRCULO>', style='cyan')
    print(panel)


if __name__ == '__main__':
    main()
