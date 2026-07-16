def metade(preço):
    """
    -> Calcula a metade de um numero
    :param n: numero
    :return: retorna a metade
    """
    res = preço / 2
    return res


def dobro(preço):
    """
    -> Calcula o dobro de um numero
    :param n: numero
    :return: retorna o dobro
    """
    res = preço * 2
    return res


def aumentar(preço, taxa):
    """
    -> Calcula um aumento de um numero baseado na porcentagem
    :param n: numero
    :param p: porcentagem
    :return: numero aumentado
    """
    res = preço + (preço * taxa / 100)
    return res


def diminuir(preço, taxa):
    """
    -> Calcula uma diminuição de um numero baseado na porcentagem
    :param n: numero
    :param p: porcentagem
    :return: numero diminuido
    """
    res = preço - (preço * taxa / 100)
    return res


def moeda(n):
    res = f'R${n:.2f}'.replace('.', ',')
    return res