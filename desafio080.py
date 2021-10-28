numeros = []
for c in range(0,5):
    numero = int(input('Digite um número :'))
    if c==0 or numero > numeros[-1]:
        numeros.append(numero)
        print('Adicionado ao final da lista.')
    else:
        pos=0
        while pos < len(numeros):
            if numeros[pos]>numero:
               numeros.insert(pos,numero)
               print(f'Adicionado na posição {pos} da lista.')
               break
            pos+=1
print(f'Números digitados {numeros}')