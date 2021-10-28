numero = int(input('Digite um número entre 1 e 9999: '))
# Fazendo a divisão inteira do número por 1 e depois fazendo o módulo(resto da divisão) do resultado por 10 vai restar a unidade do número
unidade = numero //1% 10
# Fazendo a divisão inteira do número por 10 e depois fazendo o módulo(resto da divisão) do resultado por 10 vai restar a dezena do número
dezena  = numero // 10 %10
# Fazendo a divisão inteira do número por 100 e depois fazendo o módulo(resto da divisão) do resultado por 10 vai restar a centrena do número
centena = numero // 100 %10
# Fazendo a divisão inteira do número por 1000 e depois fazendo o módulo(resto da divisão) do resultado por 10 vai restar a milhar do número
milhar = numero //1000 % 10

print('Analisando o número {} '.format(numero))
print('A unidade é {}.'.format(unidade))
print('A dezena é {}.'.format(dezena))
print('A centena é {}.'.format(centena))
print('O milhar é {}.'.format(milhar))