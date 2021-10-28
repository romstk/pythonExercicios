from random import shuffle
n1 = str(input('Nome do primeiro nome: '))
n2 = str(input('Nome do segundo nome: '))
n3 = str(input('Nome do terceiro nome: '))
n4 = str(input('Nome do quarto número: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A orderm de apresentação dos trabalhos será {}.'.format(lista))
