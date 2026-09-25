from rich import print
class Livro:
    paginaAtual = 1
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        return print(f":book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[blue]' que tem [green]{self.paginas} páginas [blue]no total. Você agora está na [green]página {Livro.paginaAtual}[/]")

    def avancar_paginas(self, quant):
        if Livro.paginaAtual + quant:
        Livro.paginaAtual += quant
        return print(f"{Livro.paginaAtual}..")

l1 = Livro("Livro 1", 10)
l1.avancar_paginas(5)
