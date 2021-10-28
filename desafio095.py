jogador = dict()
gols=list()
time = list()
resp='S'
while resp in 'S':
    jogador.clear()
    jogador['nome']=str(input('Nome: ')).strip().upper()
    jogador['partidas']=int(input('Número de partidas: '))
    totalgols=0
    if jogador['partidas']>0:
        for c in range(0, jogador['partidas']):
            gols.append(int(input(f'Quantos gols na {c+1}ª partida ? ')))
            totalgols+=gols[c]
        jogador['gols']=gols.copy()
        jogador['totalgols']=totalgols
    else:
        jogador['totalgols'] = totalgols
        jogador['gols']=0
    time.append(jogador.copy())
    gols.clear()
    while True:
        resp = str(input('Deseja continuar [S/N]?')).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print('Opção inválida. informe S ou N: ')
print('-='*30)
print(f'{"cod":>4} ', end='')
for k in jogador.keys():
    print(f'{k:<15}',end='')
print()
print('-='*30)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-='*30)
while True:
    resp=int(input('Mostrar dados de qual jogador? (999 encerra>) '))
    if resp==999:
        break
    else:
          if 0 <= resp <= len(time):
            print(f' --LEVANTAMENTO DO JOGADOR {time[resp]["nome"]}:' )
            print(f'Jogou {time[resp]["partidas"]} partidas.')
            if time[resp]['partidas']>0:
               for c in time[resp]['gols']:
                print(f'=> Na partida {time[resp]["gols"].index(c)} fez {c} gols.')
          else:
                print('Não existe jogador com este código.')
print('<<<Programa finalizado!>>>')
