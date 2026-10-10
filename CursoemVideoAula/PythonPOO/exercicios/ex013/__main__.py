from classes import *

def main():
    p1 = Mae('Jaciara')
    p2 = Filho('Matheus')
    p3 = Filha('Mônica')

    print('-=' * 30)
    p1.fazer_pudim()
    p1.fritar_coxinha()

    print('-=' * 30)
    p2.fazer_pudim()
    p2.fritar_coxinha()

    print('-=' * 30)
    p3.fazer_pudim()
    p3.fritar_coxinha()

    print('-=' * 30)



if __name__ == '__main__':
    main()