frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A palavra \033[1;31m{}\033[m é um palíndromo'.format(junto))
else:
    print('A palavra \033[1;31m{}\033[m não é um palíndromo'.format(junto))
