class Retangulo:

    def __init__(self, base = 1, altura = 1):
        self.base = base
        self.altura = altura
        self.area = self.base * self.altura
        self._base = self.base
        self._altura = self.altura
        self._area = None
        self.medidas = f'Base = {self.base}\nAltura = {self.altura}\nÁrea = {self.area}'

