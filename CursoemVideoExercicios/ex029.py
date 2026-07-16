km = float(input('Qual a velocidade do carro? '))
if km > 80:
    km = km - 80
    multa = km * 7
    print('\033[1;31mSua multa foi de R${:.2f}'.format(multa))
else:
    print('\033[1;32mVocê está dirigindo dentro do limite de velocidade! PARABÉNS!')