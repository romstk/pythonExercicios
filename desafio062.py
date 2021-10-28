print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termos=10
contador=1
controle=1

while controle >0:
    while contador <= termos:
        print(termo, end='->')
        termo+=razao
        contador+=1
    print(' PAUSA ')
    controle=int(input('Quantos termos deseja mosrar mais ?  '))
    termos +=controle

print('Foram analisados {} termos. '.format(termos))
print('Fim!')
