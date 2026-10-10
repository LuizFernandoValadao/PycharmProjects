from functools import singledispatchmethod

class Analisador:

    @singledispatchmethod
    def analisar(self, valor):
        print(f'Não foi possível analisar o valor {valor}')

    def analisar(self, valor: int):
        print(f'{valor} é um número Inteiro')

    def analisar(self, valor: str):
        print(f'{valor} é uma cadeia de caracteres')