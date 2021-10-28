jogador = dict()
gols=list()
jogador['nome']=str(input('Nome: ')).strip().upper()
jogador['partidas']=int(input('Número de partidas: '))
totalgols=0
if jogador['partidas']>0:
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na {c+1}ª partida ? ')))
        totalgols+=gols[c]
    jogador['gols']=gols
    jogador['totalgols']=totalgols
else:
    jogador['totalgols'] = totalgols
    jogador['gols']=0
print('-='*40)
print(jogador)
print('-='*40)
for k, v in jogador.items():
    print(f'{k} tem o valor {v}')
print('-='*40)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
if jogador['partidas']>0:
    for c in jogador['gols']:
        print(f'=> Na partida {gols.index(c)+1} fez {c}')

print(f'Foi um total de {jogador["totalgols"]} de gols. ')
