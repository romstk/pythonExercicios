lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? S/N')).strip().upper()[0]
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar? S/N')).strip().upper()[0]
    if resp in 'Nn':
        break
print(f'A listagem de números informados é {lista}')
c=0
while c < len(lista):
      if lista[c]%2==0:
          pares.append(lista[c])
          c+=1
      else:
          impares.append(lista[c])
          c+=1
print(f'Listagem de números ímpares {impares}.')
print(f'Listagem de números ímpares {pares}.')