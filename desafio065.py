contador=1
numero = int(input('Informe o {}° número inteiro: '.format(contador)))
maior=menor=soma=media=numero
flag=str(input('Deseja continuar ? [S/N]'))
while flag in 'Ss':
    contador += 1
    '''Informando uma fstring - formatando a string com a interpolação da variável dentro das chaves'''
    numero = int(input(f'Informe o {contador}° número inteiro: '))
    if numero>maior:
       maior=numero
    if numero<menor:
       menor=numero
    flag = str(input('Deseja continuar ? [S/N]'))
    soma+=numero
media=soma/contador
print('Foram lidos {} numeros, sendo o maior {}, o menor {} e a média {}. '.format(contador, maior, menor, media))


