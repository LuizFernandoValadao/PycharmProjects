from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    def preparar(self):
        print("--- Iniciando o Preparo ---")

        print(f'1. {self.ferver_agua()}')
        print(f'2. {self.misturar()}')
        print(f'3. {self.servir()}')

        print("--- Bebida Pronta ---")

    def ferver_agua(self):
        return f'Fervendo água a 100 graus Celsius.'

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):

    def misturar(self):
        return f'Passado água pressurizada pelo pó de café moido.'

    def servir(self):
        return f'Servindo em xícara pequena.'


class Cha(BebidaQuente):

    def misturar(self):
        return f'Mergulhando o sachê de ervas na água.'

    def servir(self):
        return f'Servindo na caneca de porcelana com limão.'


class Leite(BebidaQuente):

    def misturar(self):
        return f'Passando vapor pressurizado pelo bico do leite.'

    def servir(self):
        return f'Servindo na caneca grande, já com café.'