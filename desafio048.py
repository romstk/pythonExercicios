print('Calculando a soma de todos os valores Ímpares divisíveis por 3 entre 1 e 500. ')
soma=0
cont=0
for c in range(1,501,2):
    if c%3==0:
        soma+=c
        cont+=1
print('A soma dos {} valores solicitados é : {}'.format(cont,soma))
