numeros = [[],[]]
for c in range(1,8):
    numero = (int(input(f'Digite o {c}º número: ')))
    if numero %2==0:
       numeros[0].append(numero)
    else:
       numeros[1].append(numero)

numeros[0].sort()
numeros[1].sort()

print(f'Números pares {numeros[0]}')
print(f'Números ímpares {numeros[1]}')