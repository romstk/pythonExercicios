from random import randint

numeros = (randint(1, 100),randint(1, 100),randint(1, 100),randint(1, 100),randint(1, 100))

for pos, numero in enumerate(numeros):
    if pos == 0:
        menor = numeros[0]
        maior = numeros[0]
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f'A numeração gerada foi: {numeros}')
print(f'O maior número da lista é {maior} e o menor é {menor}.')
