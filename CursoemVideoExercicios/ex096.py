def area(l, c):
    a = l * c
    print(f'A área de um terreno \033[1;33m{l:.1f}x{c:.1f}\033[m é de \033[1;31m{a:.1f}m²\033[m.')


print(' Controle de Terrenos')
print('-'*22)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
print('-'*45)
