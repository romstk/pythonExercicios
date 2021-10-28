print('CALCULANDO A TABUADA')
numero = int(input('Digite um número de 1 a 10 : '))
print('-'*12)

if 1 <= numero <= 10:
    for c in range(1,11):
        print('{} x {:2} = {}'.format(numero,c,numero*c))
else:
    print('Número inválido, tente novamente.')

print('-'*12)