salario = float(input('Qual o seu salario: R$'))
if salario <= 1250:
    salario = salario + (salario * 15 / 100)
else:
    salario = salario + (salario * 10 / 100)
print("O seu novo salario é de \033[32mR${:.2f}\033[m".format(salario))