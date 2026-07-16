#Calcula o aluguel do carro alugado baseado nos dias e nos quilometros percorridos!

d = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
print('O total a pagar é de R${:.2f}'.format((d*60)+(km*0.15)))
