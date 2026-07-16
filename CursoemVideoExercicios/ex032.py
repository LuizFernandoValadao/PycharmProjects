from datetime import date

ano = int(input('Qual ano estamos? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é \033[1;32mbissexto'.format(ano))
else:
    print('O ano {} não é \033[1;31mbissexto'.format(ano))