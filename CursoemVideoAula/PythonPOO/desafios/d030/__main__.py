from credencial import *

def main():
    c = Credencial()
    c.senha = str(input('Digite a sua senha: '))
    print(c.senha)
    c.validar('CeV!@')

if __name__ == '__main__':
    main()