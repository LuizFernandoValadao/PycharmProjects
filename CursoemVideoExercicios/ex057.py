sexo = str(input('Informe seu sexo: [M/F]  ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
