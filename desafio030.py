numero = int(input('Digite um número inteiro: '))
rest= numero%2

print('Resto {}'.format(rest))

if rest>0:

    print('Número IMPAR.')
else:
    print('Número PAR.')