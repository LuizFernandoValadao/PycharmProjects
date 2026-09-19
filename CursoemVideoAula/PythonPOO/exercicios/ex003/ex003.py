class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depositos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criado com sucesso. Saldo atual de R$ {self.saldo:,.2f}')

    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem \033[32mR${self.saldo:,.2f}\033[m de saldo'

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:,.2f} autorizado na conta {self.id}')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

        else:
            print(f'\033[1;31mSaque de R${valor:,.2f} Negado na conta {self.id}: Saldo insuficiente\033[m')


c1 = ContaBancaria(112, 'Gustavo', 3000)
print(c1)
c1.depositar(500)
print(c1)
c1.sacar(4000)
print(c1)