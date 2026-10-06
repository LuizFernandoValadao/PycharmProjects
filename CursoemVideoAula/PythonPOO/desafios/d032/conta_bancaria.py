from hashlib import sha256

class ContaBancaria:

    def __init__(self, id, nome, saldo, senha = ""):
        if senha == "" or len(senha) <= 0:
            senha = str(input('Senha: '))

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
        self._titular = nome

    def depositar(self, valor):
        if valor <= 0 or not isinstance(valor, int):
            raise ValueError('Valor deve ser positivo')
        else:
            self.__saldo += valor
            print(f'Depósito de R${valor:,.2f} autorizado na conta {self._id}')

    def pede_senha(self) -> str:
        senha = str(input('Senha: '))

    def sacar(self, valor:float, chave: str = None):
        if valor <= 0 :
            raise ValueError('Valor deve ser um número positivo')
        if valor > self.__saldo:
            print(f'Não foi possivel sacar, Valor maior que o saldo. Saldo atual de R${self.__saldo:,.2f}')
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self._id}")

    def validar_senha(self, chave: str) -> bool:
        pass