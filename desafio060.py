print('---CALCULO DE FATORIAL---')
n = int(input('Informe um número para cálculo do seu fatorial: '))
f = 1
print('Calculando {}! => '.format(f), end=' ')

while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    f = f * n
    n -= 1

print(f)
