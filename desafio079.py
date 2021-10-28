numeros = []
while True:
    numero = int(input('Digite um número: '))
    if numero not in numeros:
       numeros.append(numero)
       print('Núemro incluído na lista.')
    else:
       print('Número já informado. Não foi adicionado.')
    op=str(input('Deseja continuar ? S/N'  )).strip().upper()[0]
    while op not in 'SsNn':
       op = str(input('Opção inválida. Informe opação se deseja continuar ? S/N  ')).strip().upper()[0]
    if op =='N':
        break
numeros.sort()
print(f'Números informados {numeros}')
