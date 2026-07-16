peso = float(input('Digite o seu peso: '))
menor = peso
maior = peso
for c in range(1, 5):
    peso = float(input('Digite o seu peso: '))
    if peso < menor:
        menor = peso
    elif peso > maior:
        maior = peso

print('O MAIOR peso é {:.1f}KG\nO MENOR peso é {:.1f}KG'.format(maior, menor))