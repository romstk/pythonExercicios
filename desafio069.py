pessoasmaisdezoito=0
quanthomens=0
mulheresmensvinte=0
print('-'*23)
print('- CADASTRO DE PESSOAS -')
print('-'*23)
while True:
    idade = int(input('Informe sua idade: '))
    while True:
        sexo = str(input('Informe o sexo [M/F] ')).strip().upper()[0]
        if sexo in 'FM':
            break
    print('-' * 20)
    if idade > 18:
       pessoasmaisdezoito+=1
    if sexo=='F' and idade <20:
           mulheresmensvinte+=1
    if sexo=='M':
        quanthomens+=1
    while True:
        continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if continua in 'SsNn':
            break
    if continua=='N':
        break
print(f'Dos dados lidos,  {pessoasmaisdezoito} são pessoas maires de 18 anos, {quanthomens} são homens e {mulheresmensvinte} mulheres com mais de 20 anos. ')