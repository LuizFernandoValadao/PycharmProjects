casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual é o seu  salario? R$'))
anos = int(input('Quantos anos deseja pagar? '))
mensalidade = casa / (anos * 12)
if mensalidade <= salario * 30 / 100:
    print('\033[32mVoce poderá comprar essa casa!')
else:
    print('\033[31mVocê não poderá comprar essa casa!')