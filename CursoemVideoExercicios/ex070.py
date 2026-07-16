soma = 0
maisdemil = 0
print('='*40)
print('           LOJA SUPER BARATÃO')
print('='*40)
produto = str(input('Digite o nome do produto: '))
valor = float(input('Preço: R$'))
menor = valor
produto_barato = produto
soma += valor
if valor > 1000:
    maisdemil += 1
continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
while continuar not in 'SN':
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
if continuar == 'S':
    while True:
        produto = str(input('Digite o nome do produto: '))
        valor = float(input('Preço: R$'))
        soma += valor
        if valor < menor:
            menor = valor
            produto_barato = produto
        if valor > 1000:
            maisdemil += 1
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        while continuar not in 'SN':
            continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if continuar == 'N':
            break
print('----------- FIM DO PROGRAMA ------------')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {maisdemil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_barato} que custa R${menor:.2f}')
