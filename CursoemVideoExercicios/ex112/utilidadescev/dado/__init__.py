def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: \"{entrada}\" é um preço invalido!\033[m')
        else:
            válido = True
    return float(entrada)

