def dobra(lst):
    for pos in range(0, len(lst)):
        lst[pos] *= 2


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)