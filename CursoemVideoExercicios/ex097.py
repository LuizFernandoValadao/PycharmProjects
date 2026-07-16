def escreva(txt):
    for t in txt:
        print('\033[1;31m~' * len(t))
        print(f'\033[1;34m{t} ')
        print('\033[1;31m~' * len(t))

titulo = list()
titulo.append(' Gustavo Guanabara ')
titulo.append(' Curso de Python no Youtube ')
titulo.append(' Cev ')
escreva(titulo)