homem = 0
maior = 0
mulheres = 0
while True:
    print('-'*28)
    print('    CADASTRE UMA PESSOA')
    print('-'*28)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    print('-'*28)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo tivemos {homem} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')