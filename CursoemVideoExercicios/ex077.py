palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'Na palavra \033[1;34m{p.upper()}\033[m temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
    print('')