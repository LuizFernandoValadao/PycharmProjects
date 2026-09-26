from rich import print
from time import sleep
class Livro:
    paginaAtual = 1
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        return print(f":book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[blue]' que tem [green]{self.paginas} páginas [blue]no total. Você agora está na [green]página {Livro.paginaAtual}[/]")

    def avancar_paginas(self, quant):
        pgatual = Livro.paginaAtual + quant
        if pgatual > self.paginas:
            pgrest = self.paginas - Livro.paginaAtual
            pgatual = self.paginas
            while Livro.paginaAtual < pgatual:
                Livro.paginaAtual += 1
                print(f'Pág{Livro.paginaAtual} ▶️', end=' ')
                sleep(0.5)
            print(f'[blue]Você avançou {pgrest} páginas e agora está na [green]página {Livro.paginaAtual}[/]')
            print(f"[red]:police_car_light: Você chegou ao final do livro '{self.titulo}'[/]")
        else:
            while Livro.paginaAtual < pgatual:
                Livro.paginaAtual += 1
                print(f'Pág{Livro.paginaAtual} ▶️', end=' ')
                sleep(0.5)
            print(f'[blue]Você avançou {quant} páginas e agora está na [green]página {Livro.paginaAtual}[/]')


l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)