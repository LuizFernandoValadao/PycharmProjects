from classes import *

def main():
    a = Cachorro("Bruce")
    b = Gato("Mister")
    c = Pato('Patinho')
    d = Galinha('Frango')
    e = Spitz('Luluzinha')
    f = PitBull('Guerreiro')

    a.emitir_som()
    b.emitir_som()
    c.emitir_som()
    d.emitir_som()
    e.emitir_som()
    f.emitir_som()


if __name__ == '__main__':
    main()