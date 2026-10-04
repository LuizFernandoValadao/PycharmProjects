class Retangulo:

    def __init__(self, base = 1, altura = 1):
        self._base = base
        self._altura = altura
        self._area = None

        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if not isinstance(base, float) and not isinstance(base, int):
            raise TypeError('O valor deve ser um número')
        if base < 0:
            raise ValueError('Valor inválido para a base!')
        else:
            self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if not isinstance(altura, float) and not isinstance(altura, int):
            raise TypeError('O valor deve ser um número')
        if altura < 0:
            raise ValueError('Valor inválido para a altura!')
        else:
            self._altura = altura

    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area

    @area.setter
    def area(self):
        raise PermissionError('Área não pode ser configurada desse jeito')

    @property
    def medidas(self):
        return f'Base = {self._base}\nAltura = {self._altura}\nÁrea = {self._area}'

    @medidas.setter
    def medidas(self, medidas:tuple):
        self.base = medidas[0]
        self.altura = medidas[1]
        self._area = self._base * self._altura
