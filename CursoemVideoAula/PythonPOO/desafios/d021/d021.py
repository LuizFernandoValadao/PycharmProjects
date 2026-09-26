from rich import print

class Caneta:
    def __init__(self, cor = 'azul'):
        self.cor = cor
        self.aberta = False

    def cores(self):
        if self.cor == 'azul':
            self.cor = '[blue]'
        if self.cor == 'vermelha':
            self.cor = '[red]'
        if self.cor == 'verde':
            self.cor = '[green]'

    def destampar(self):
        self.aberta = True
        return self.aberta

    def escrever(self, texto):
        if self.aberta:
            self.cores()
            print(f'{self.cor}{texto}', end='')
        else:
            self.cores()
            print(f'A {self.cor}caneta[/] está tampada!', end='')

    def quebrar_linha(self, quant):
            print('\n'*quant)

c1 = Caneta('azul')
c2 = Caneta('vermelha')
c3 = Caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá, tudo bem?')
c1.quebrar_linha(2)
c2.escrever('Olá, Gafanhoto!')
c3.escrever('Vamos exercitar!')