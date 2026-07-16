#calcula o seno, cosseno e a tangente de um ãngulo!

from math import sin, cos, tan, radians

ang = float(input('Digite o valor do angulo: '))
print('Seno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(sin(radians(ang)),cos(radians(ang)),tan(radians(ang))))
