def ficha(nome='Desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gols durante o campeonato.')
print('-'*30)
nome=str(input('Nome do jogador: '))
gols=str(input('Número de gols: '))
if gols.isnumeric():
    gols=int(gols)
else:
    gols=0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome,gols)


