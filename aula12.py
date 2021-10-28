nome = str(input('Qual é o seu nome ?  '))
print('Bom dia, {}!'.format(nome))

if nome=='Ricardo':
    print('Nossa! Que nome mais lindo...')
elif nome=='Maria' or nome=='Pedro' or nome=='Ana' or nome=='Rosa':
    print('Seu nome é bastante popular no Brasil. ')
else:
    print('Seu nome é bem normal. ')
print('Tenha um bom dia.')