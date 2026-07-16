números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n1 = int(input('Digite um número entre 0 e 20: '))
while n1 < 0 or n1 > 20:
    n1 = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print('=-'*20)
print(f'Seu número por extenso fica {números[n1]}')