print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c=1
while c <= 10:
    print(termo, end='->')
    termo+=razao
    c +=1
print('Fim!')
