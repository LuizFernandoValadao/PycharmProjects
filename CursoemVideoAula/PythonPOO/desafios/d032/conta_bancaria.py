from hashlib import sha256
from pwinput import pwinput
from rich import print
from rich.panel import Panel


class ContaBancaria:

    def __init__(self, id: int, nome:str = None, saldo: float = 0, senha = ""):
        if senha == "" or len(senha) <= 0:
            senha = str(pwinput('Senha: ', mask='*'))

        self._id = id
        self._titular = nome
        self.__saldo = saldo
        self.__hash = sha256(senha.encode("utf-8")).hexdigest()
        print(f'Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}')


    @property
    def nome(self):
        return self._titular


    @nome.setter
    def nome(self, nome):
        if self.pede_senha():
            self._titular = nome
            print(f'Nome alterado para {self._titular}!')
        else:
            print(f'Senha incorreta, não foi possivel alterar o nome!')

    def depositar(self, valor):
        if valor <= 0 or not isinstance(valor, int):
            raise ValueError('Valor deve ser positivo')
        else:
            self.__saldo += valor
            print(f'Depósito de R${valor:,.2f} autorizado na conta {self._id}')


    def pede_senha(self) -> str:
        senha = str(pwinput('Senha: ', mask='*'))
        return self.validar_senha(senha)


    def sacar(self, valor:float, chave: str = None):
        if valor <= 0 :
            raise ValueError('Valor deve ser um número positivo')
        if valor > self.__saldo:
            c = Panel.fit(f'[red]Não foi possivel sacar, Valor maior que o saldo. Saldo atual de R${self.__saldo:,.2f}[/]')
            print(c)
        else:
            if chave != None:
                if self.validar_senha(chave):
                    self.__saldo -= valor
                    c = Panel.fit(f"[green]Saque de R${valor:,.2f} autorizado na conta {self._id}[/]")
                    print(c)
                else:
                    c = Panel.fit('[red]Senha não confere. Saque não autorizado![/]')
                    print(c)
            else:
                if self.pede_senha():
                    self.__saldo -= valor
                    c = Panel.fit(f"[green]Saque de R${valor:,.2f} autorizado na conta {self._id}[/]")
                    print(c)
                else:
                    c = Panel.fit('[red]Senha não confere. Saque não autorizado![/]')
                    print(c)



    def validar_senha(self, chave: str) -> bool:
        chave = sha256(chave.encode("utf-8")).hexdigest()
        if chave == self.__hash:
            return True
        else:
            return False

    def __str__(self):
        return f"A conta {self._id} de {self._titular} tem R${self.__saldo:,.2f} de saldo."