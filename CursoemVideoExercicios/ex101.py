def voto(i):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - i
    if idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    elif idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    elif idade >= 16:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: VOTO NEGADO!')


print('-'*30)
ano_nasc = int(input('Em que ano você nasceu? '))
voto(ano_nasc)