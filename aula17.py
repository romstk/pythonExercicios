#num = [2,5,9,1]
#print(num)
#num[2]=3
#print(num)
#num.append(7)
#num.sort()
#print(num)
#num.sort(reverse=True)
#num.insert(2,0)
#print(num)
#print(f'Esta lista possui {len(num)} elementos.')
numeros = []

for n in range(0,5):
    numeros.append(int(input('Digite um valor: ')))


for c, v in enumerate(numeros):
        print(f'Na posição {c} encontrei o valor {v}')
print('Fim.')



