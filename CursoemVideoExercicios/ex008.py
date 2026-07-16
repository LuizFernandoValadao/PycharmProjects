#Converte diferentes comprimentos!

m = float(input('Quantos Metros: '))
print('A medida de {:.1f} m corresponde a \n{:.3f}km \n{:.2f}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(m ,m/1000, m/100, m/10, m*10, m*100, m*1000))
