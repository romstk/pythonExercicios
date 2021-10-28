salario = float(input('Informe o salário para calcularmos o aumento: '))

if salario > 1250:
    salario = salario+(salario*10/100)
    print('Você ganhou um aumento de 10% e seu salário agora é R$ {:.2f}'.format(salario))
else:
    salario = salario+(salario*15/100)
    print('Você ganhou um aumento de 15% e seu salário agora é R$ {:.2f}'.format(salario))
