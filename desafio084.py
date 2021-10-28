pessoas = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas)==0:
        maior=menor=dados[1]
    else:
        if dados[1]>maior:
           maior=dados[1]
        if dados[1]<menor:
           menor=dados[1]
    pessoas.append(dados[:])
    dados.clear();
    resp = str(input('Cadastrar mais um? S/N ')).strip().upper()[0]
    while resp not in 'SsNN':
        resp = str(input('Resposta inválida. Informe? S/N ')).strip().upper()[0]
    if resp=='N':
        break
print('*'*30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior} e o menor peso foi {menor}. ')
pesadas = list()
leves = list()
for p in pessoas:
    if p[1]==maior:
        pesadas.append(p[0])
    elif p[1]==menor:
        leves.append(p[0])
print(f'Mais pesadas são {pesadas} e mais leves {leves} pessoas. ')




