soma=0
cont=0
for c in range(0,6):
    numero = int(input('Digite um número: '))
    if numero%2==0:
        print('Número digitado é par. Será somado.')
        soma+=numero
        cont+=1
    else:
        print('Número digitado é impar. Não será somando.')

print('Contagem final foi de {} números pares somando um total de {}. '.format(cont,soma))