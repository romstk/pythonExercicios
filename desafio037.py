numero = int(input('Informe um número inteiro: '))
print('''Informe as seguintes opções de conversão:
[1] Binario
[2] Octal
[3] Hexadecimal''')
opt = int(input('Sua opção: '))


if opt==1:
   print('O número {} convertido para binário corresponde a : {}'.format(numero, bin(numero)[2:]))
elif opt==2:
   print('O número {} convertido para octal corresponde a : {}'.format(numero, oct(numero)[2:]))
elif opt==3:
   print('O número {} convertido para hexadecimal corresponde a : {}'.format(numero, hex(numero)[2:]))
else:
   print('Opção selecionada inválida. Infome os dados novamente. ')