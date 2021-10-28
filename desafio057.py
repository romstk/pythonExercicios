sexo = str(input('Informe o sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido. Por favor informe o sexo: [M/F]')).strip().upper()[0]
print('Sexo informado {} cadastrado com sucesso.'.format(sexo))

