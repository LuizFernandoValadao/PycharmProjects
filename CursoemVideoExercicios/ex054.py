from datetime import date

ano_atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    ano_nasc = int(input('Digite o ano de nascimento: '))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1
print('\033[1;32mTem {} pessoas maiores de idade'.format(maior))
print('\033[1;34mTem {} pessoas menores de idade'.format(menor))