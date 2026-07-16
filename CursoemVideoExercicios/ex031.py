km = float(input('Qual vai ser a distancia da viagem em km/h: '))
if km <= 200:
    preco = km * 0.50
    print('O Preço da viagem vai ser \033[1;32mR${:.2f}'.format(preco))
else:
    preco = km * 0.45
    print('O Preço da viagem vai ser \033[1;32mR${:.2f}'.format(preco))