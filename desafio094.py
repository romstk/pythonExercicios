dados = dict()
pessoas = list()
resp='S'
soma=0
while resp=='S':
    dados.clear()
    dados['nome'] = str(input('Nome: ')).strip().lower().capitalize()
    while True:
        dados['sexo']=str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        else:
            print('Por favor, digite apenas F ou M para o sexo. ')
    dados['idade']=int(input('Idade: '))
    soma+=dados['idade']
    while True:
        resp=str(input('Ler outro? S/N')).strip().upper()[0]
        if resp in "SNsn":
            break
        else:
            print('ERRO! Tente novamente. ')
    pessoas.append(dados.copy())
    media=soma/len(pessoas)
print('-='*30)
print(f'A) Foram cadastradas {len(pessoas)} pessoas. ')
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print()

print('D) Lista das pessoas que estão acima da média de idade: ')


for p in pessoas:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ',end=' ')
        print()

print('<<<ENCERRADO>>>')


