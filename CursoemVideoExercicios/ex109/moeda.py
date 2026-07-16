def metade(preço=0, formato=False):
    """
    -> Calcula a metade de um numero
    :param n: numero
    :return: retorna a metade
    """
    res = preço / 2
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    """
    -> Calcula o dobro de um numero
    :param n: numero
    :return: retorna o dobro
    """
    res = preço * 2
    return res if formato is False else moeda(res)


def aumentar(preço=0, taxa=0, formato=False):
    """
    -> Calcula um aumento de um numero baseado na porcentagem
    :param n: numero
    :param p: porcentagem
    :return: numero aumentado
    """
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    """
    -> Calcula uma diminuição de um numero baseado na porcentagem
    :param n: numero
    :param p: porcentagem
    :return: numero diminuido
    """
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')