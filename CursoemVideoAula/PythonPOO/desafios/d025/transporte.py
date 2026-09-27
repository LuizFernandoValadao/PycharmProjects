from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia, frete):
        self.distancia = distancia
        self.frete = frete

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50
    def __init__(self, distancia, frete = fator):
        super().__init__(distancia, frete)

    def calcular_frete(self):
        return f'R${self.frete * self.distancia:.2f}'


class Caminhao(Transporte):
    fator = 1.20
    def __init__(self, distancia, frete = fator):
        super().__init__(distancia, frete)

    def calcular_frete(self):
        if self.distancia <= 50:
            return f'Raio minimo de 50Km'
        else:
            return f'R${self.frete * self.distancia:.2f}'


class Drone(Transporte):
    fator = 9.50
    def __init__(self, distancia, frete = fator):
        super().__init__(distancia, frete)

    def calcular_frete(self):
        if self.distancia > 10:
            return f'Raio maximo de 10Km'
        else:
            return f'R${self.frete * self.distancia:.2f}'