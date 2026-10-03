from diario import *
from rich import print, inspect

def main():
    d = Diario('Gafanhoto')

    d.escrever('Primeira mensagem')
    d.escrever('Você é uma pessoa simpática')
    d.escrever('Você gosta de Python')

    inspect(d, private=True, methods=True)
    try:
        d.ler('Gafanhoto')
    except Exception as e:
        print(f'[red] ERRO: {e}')


if __name__ == '__main__':
    main()