lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#Tuplas são imutáveis
#lanche[1] = 'Pudim'
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')

print(sorted(lanche))