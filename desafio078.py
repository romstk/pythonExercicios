numeros = []
for cont in range(0,5):
    numeros.append(int(input('Digite um número: ')))
maior = max(numeros)
menor = min(numeros)
print(f'A lista de números digitados é {numeros} contendo {len(numeros)} elementos.')
print(f'Maior valor é {maior} nas posições: ',end='')
for i, v in enumerate(numeros):
    if v==maior:
        print(f'{i}', end='... ')
print()
print(f'Menor valor {menor} nas posições: ',end='')
for i,v in enumerate(numeros):
    if v==menor:
        print(f'{i}',end='... ')