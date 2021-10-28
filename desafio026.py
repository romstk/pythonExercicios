nome = str(input('Digite uma frase: ')).upper().strip()
contaA = nome.count('A')

print('O nome digitado foi {}'.format(nome))
print('Possui {} letra A'.format(contaA))
print('O primeiro "A" aparece na posição {}'.format(nome.find('A')+1))
print('O último "A" aparece na posição {}'.format(nome.rfind('A')+1))