print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
resto_50 = 0
resto_20 = 0
resto_10 = 0
valor = int(input('Que valor você quer sacar? R$ '))
if valor // 50 >= 1:
    print(f'Total de {valor // 50} cédulas de R$50 ')
    resto_50 = valor % 50
    if resto_50 // 20 >= 1:
        print(f'Total de {resto_50 // 20} cédulas de R$20 ')
        resto_20 = resto_50 % 20
        if resto_20 // 10 >= 1:
            print(f'Total de {resto_20 // 10} cedulas de R$10 ')
            resto_10 = resto_20 % 10
            if resto_10 // 1 >= 1:
                print(f'Total de {resto_10 // 1} cedulas de R$1 ')
        else:
            if resto_20 // 1 >= 1:
                print(f'Total de {resto_20 // 1} cédulas de R$1 ')
    elif resto_50 // 10 >= 1:
        print(f'Total de {resto_50 // 10} cédulas de R$10 ')
        resto_10 = resto_50 % 10
        if resto_10 // 1 >= 1:
            print(f'Total de {resto_10 // 1} cédulas de R$1 ')
    else:
        if resto_50 // 1 >= 1:
            print(f'Total de {resto_50 // 1} cédulas de R$1 ')
elif valor // 20 >= 1:
    print(f'Total de {valor // 20} cédulas de R$20 ')
    resto_20 = valor % 20
    if resto_20 // 10 >= 1:
        print(f'Total de {resto_20 // 10} cédulas de R$10 ')
        resto_10 = resto_20 % 10
        if resto_10 // 1 >= 1:
            print(f'Total de {resto_10 // 1} cédulas de R$1 ')
    else:
        if resto_20 // 1 >= 1:
            print(f'Total de {resto_20 // 1} cédulas de R$1 ')
elif valor // 10 >= 1:
    print(f'Total de {valor // 10} cédulas de R$10 ')
    resto_10 = valor % 10
    if resto_10 // 1 >= 1:
        print(f'Total de {resto_10 // 1} cédulas de R$1 ')
else:
    print(f'Total de {valor // 1} cédulas de R$1 ')
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')