r = "S"
tot = 0
maior = 0
menor = 0
m = 0
while r == "S":
    n2 = int(input('Digite um número:'))
    if tot == 0:
        maior = n2
        menor = n2
    if maior < n2:
        maior = n2
    elif menor > n2:
        menor = n2
    tot += 1
    m += n2
    r = str(input('Quer continuar? [S/N]')).upper().strip()
print('Foi digitados {} números e a média deles é {:.2f}'.format(tot, m/tot))
print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado foi {}'.format(menor))