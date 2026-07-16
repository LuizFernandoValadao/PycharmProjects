#Calcula a hipotenusa de um triangulo retangulo!

import math

ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
print('O comprimento da hipotenusa vai ser {:.2f}'.format(math.hypot(ca,co)))
