media = 0
idadev = 0
nomevelho = ''
contador = 0
for c in range(1, 5):
    print('\033[1;34m----- {}º PESSOA -----\033[m'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo == 'M' and idade > idadev:
        idadedev = idade
        nomevelho = nome
    elif sexo == 'F' and idade < 20:
        contador += 1
    media += idade
media = media / 4
print('-=-'*20)
print('A media das idade é {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(idadedev, nomevelho))
print('Tem {} Mulheres com menos de 20 anos'.format(contador))