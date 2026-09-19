class Gafanhoto:
    def __init__(self, nome = 'vazio', idade = 0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f'{self.nome} e Gafanhoto(a) e tem {self.idade} anos de idade.'

g1 = Gafanhoto('Maria', 17)
g1.aniversario()
print(g1.__dict__)
print(g1.__getstate__  ())

g2 = Gafanhoto('Mauro', 53)
print(g2)
print(g2.__dict__)
print(g2.__class__)
