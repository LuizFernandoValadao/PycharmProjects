preço = float(input('Qual é o valor do produto: R$'))
print('\033[1;31m-\033[m'*50)
print('| \033[1;32m1\033[m - A vista \033[1;34mdinheiro ou cheque\033[m: \033[1;33m10%\033[m de desconto')
print('| \033[1;32m2\033[m - A vista no \033[1;34mcartão\033[m: \033[1;33m5%\033[m de desconto')
print('| \033[1;32m3\033[m - Em até \033[1;34m2x no cartão\033[m: preço normal')
print('| \033[1;32m4 \033[m- \033[1;34m3x ou mais\033[m no cartão: \033[1;33m20%\033[m de juros')
print('\033[1;31m-\033[m'*50)
frmpaga = int(input('Qual vai ser a forma de pagamento: '))
if frmpaga == 1:
    print('O produto vai sair por \033[1;32mR${:.2f}\033[m.'.format(preço * 0.90))
elif frmpaga == 2:
    print('O produto vai sair por \033[1;32mR${:.2f}\033[m.'.format(preço * 0.95))
elif frmpaga == 3:
    preço = preço/2
    print('Vai ficar 2 parcelas de \033[1;32mR${:.2f}\033[m.'.format(preço))
elif frmpaga == 4:
    parcela = int(input('Quantas parcelas? '))
    preço = (preço*1.2) / parcela
    print('Vai ficar {} parcelas de \033[1;32mR${:.2f}\033[m.'.format(parcela, preço))
else:
    print('\033[1;31mPor favor escolha uma forma de pagamento!')