numeros = (
            int(input('Digite um número inteiro: ')),
            int(input('Digite um número inteiro: ')),
            int(input('Digite um número inteiro: ')),
            int(input('Digite um número inteiro: '))
           )
print(f'Foram informados os seguintes números {numeros}.')

print(f'O número 9 aparece {numeros.count(9)} vezes na tupla.')

if 3 in numeros:
    print(f'O número 3 aparece na {numeros.index(3)+1}ª posição da tupla.')
else:
    print('O valor 3 não foi digitado. ')

print('Os valores pares informados foram ',end='-> ')
for c in numeros:
    if c%2==0:
        print(c,end=' ')
