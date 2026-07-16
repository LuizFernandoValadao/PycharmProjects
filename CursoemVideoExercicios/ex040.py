nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua média foi de \033[1;33m{:.1f}\033[m, \033[1;31mREPROVADO\033[m!'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média foi de \033[1;33m{:.1f}\033[m, \033[1;34mRECUPERAÇÃO\033[m!'.format(media))
else:
    print('Sua média foi de \033[1;33m{:.1f}\033[m, \033[1;32mAPROVADO\033[m!'.format(media))
