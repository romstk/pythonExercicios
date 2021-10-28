print('Vamos analisar 3 números para saber qual será o menor e o maior deles. ')
numero = float(input('Informe o primeiro número: '))
maior = numero
menor = numero
numero = float(input('Informe o segundo número: '))
if numero > maior:
    maior = numero
else:
    menor = numero
numero = float(input('Informe o terceiro número: '))
if numero > maior:
    maior = numero
else:
    if numero < menor:
        menor = numero
print('Dentre os números digitados o MAIOR foi {} e o MENOR foi {}'.format(maior, menor))
