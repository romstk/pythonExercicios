soma=0
contador = 0
flag = 0

while flag !=999:
    n=int(input('Digite um número inteiro: [999 encerra a execução] '))
    if n==999:
       flag=n
    else:
       soma+=n
       contador+=1
print('Foram informados {} números e a soma deles representa o valor {}. '.format(contador,soma))
