#Quantos baldes de tenta serão necessarios para pintar uma parede!

l = float(input('Quantos metros tem de largura: '))
a = float(input('Quantos metros tem de altura: '))
print('Serão necessarios {} litro(s) de tenta!'.format(((l*a)//2)+1))
