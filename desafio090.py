aluno = dict()
aluno['nome'] = str(input('Informe o nome: ')).strip().upper()
aluno['media'] = float(input('Informe a media: '))

if aluno['media']>=7:
   aluno['situacao']='APROVADO'
elif 5 <= aluno['media'] <7:
    aluno['situacao'] = 'RECUPERAÇÃO'
else:
    aluno['situacao']='REPROVADO'
print('-*'*30)
for k, v in aluno.items():
    print(f' -{k} é igual a {v}')
