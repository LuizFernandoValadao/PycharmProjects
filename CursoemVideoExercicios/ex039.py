from datetime import date

ano_atual = date.today().year
ano_nasc = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_nasc

if idade < 18:
    print('\033[34mVoce ainda vai se alistar!\nFaltam {} anos para o alistamento'.format(18 - idade))
elif idade > 18:
    print('\033[31mVocê já passou do tempo do alistamento!\nJá passou {} anos do tempo do alistamento'.format(idade - 18))
else:
    print('\033[32mEssa é a hora de se alistar!')