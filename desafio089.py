alunos = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')).strip().upper())
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    dados.append((dados[1]+dados[2])/2)
    alunos.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar ? S/N: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Opção inválida. Quer continuar ? S/N: ')).strip().upper()[0]
    if resp == 'N':
        break

print('-='*15)
print(f'{"No":<4}{"Nome":<20}{"Média":<8}')
print('-'*30)
#c=0
#while c < len(alunos):
#    print(f'{c:<4} {alunos[c][0]:<20} {alunos[c][3]:<8}')
#    c+=1
for c, aluno in enumerate(alunos):
    print(f'{c:<4}{alunos[c][0]:<20}{alunos[c][3]:<8}')


print('-'*30)
resp=0
while True:
    resp=int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if resp==999:
        break
    while resp > (len(alunos)-1):
        resp=int(input('Informe um número válido: '))
    print(f'Notas de {alunos[resp][0]}, [{alunos[resp][1]}, {alunos[resp][2]}]')

print('FINALIZANDO...')
print('<<<Volte sempre>>>')




