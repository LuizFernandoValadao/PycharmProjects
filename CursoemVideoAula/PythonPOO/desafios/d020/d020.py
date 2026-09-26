from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []

    def add_favoritos(self, jogo):
        self.jogos.append(jogo)

    def ficha(self):
        self.nome = self.nome.title()
        apelido = f'Jogador <{self.nick.capitalize()}>'
        conteudo = f'Nome real: [black on blue] {self.nome} [/]'
        conteudo += f'\nJogos favoritos:'
        self.jogos.sort()
        for c in range(0, len(self.jogos), 1):
            conteudo += f'\n:video_game: [blue]{self.jogos[c]}'
        painel = Panel(conteudo, title=apelido, width=40)
        print(painel)

j1 = Gamer('Fabricio da Silva', 'detonator2025')
j1.add_favoritos('Mario Bros.')
j1.add_favoritos('Sonic')
j1.add_favoritos('God of War')
j1.add_favoritos('Fortnite')
j1.ficha()

j2 = Gamer('Olivia Souza', 'peach_raivosa')
j2.add_favoritos('Mario Bros')
j2.add_favoritos('Call of Duty')
j2.ficha()