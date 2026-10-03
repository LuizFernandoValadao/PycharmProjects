class Termostato:
    def __init__(self, temperatura = 24):
        self.__temperatura = temperatura

    @property
    def ftemperatura(self):
        return f'{self.__temperatura}ºC'

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temperatura):
        if temperatura <= 16:
            self.__temperatura = 16
        elif temperatura >= 30:
            self.__temperatura = 30
        else:
            if temperatura % 0.5 != 0:
                print(f'Temperatura de {temperatura}ºC é inválida')
                '''r = temperatura % 0.5
                if r >= 0.3:
                    r = 0.5 - r
                    temperatura += r
                    self.__temperatura = temperatura
                else:
                    temperatura -= r
                    self.__temperatura = temperatura'''
            else:
                self.__temperatura = temperatura
