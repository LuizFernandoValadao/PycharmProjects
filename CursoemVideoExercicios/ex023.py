n1 = int(input('Digite um número(0 a 9999): '))
un = n1 // 1 % 10
de = n1 // 10 % 10
cent = n1 // 100 % 10
mil = n1 // 1000 % 10
print('\033[1;32mUnidade: ' , un)
print('\033[1;31mDezenas: ' , de)
print('\033[1;34mCentenas: ' , cent)
print('\033[1;35mMilhar: ' , mil)
