nome = str(input('Digite o seu nome completo: ')).strip().split()
print('O nome digitado contém as seguintes palavras {}.'.format(nome))
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[len(nome)-1]))
