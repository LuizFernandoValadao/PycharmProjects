from datetime import date

ano_atual = date.today().year
ano_nasc = int(input('Qual o ano de nascimento? '))
idade = ano_atual - ano_nasc
if idade <= 9:
    print('Você tem \033[1;33m{} anos\033[m, sua categoria é \033[1;34mMIRIM'.format(idade))
elif idade <= 14:
    print('Você tem \033[1;33m{} anos\033[m, sua categoria é \033[1;34mINFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem \033[1;33m{} anos\033[m, sua categoria é \033[1;34mJUNIOR'.format(idade))
elif idade == 20:
    print('Você tem \033[1;33m{} anos\033[m, sua categoria é \033[1;34mSÊNIOR'.format(idade))
else:
    print('Você tem \033[1;33m{} anos\033[m, sua categoria é \033[1;34mMASTER'.format(idade))