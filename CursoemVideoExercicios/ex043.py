peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('\033[1;34mAbaixo do peso!\033[m')
elif imc < 25:
    print('\033[1;32mPeso normal!\033[m')
elif imc < 30:
    print('\033[1;33mSobrepeso!\033[m')
elif imc < 40:
    print('\033[1;31mObesidade!\033[m')
else:
    print('\033[7;31;40mObesidade mórbida\033[m')
