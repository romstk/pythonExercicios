from datetime import date
funcionario = dict()
funcionario['nome']= str(input('Nome: ')).strip().upper()
funcionario['nascimento']=int(input('Ano Nascimento: '))
funcionario['idade']=date.today().year-funcionario['nascimento']
funcionario['ctps']=int(input('Carteira de Trabalho: (0 não tem) '))

if funcionario['ctps']!=0:
    funcionario['contratacao']=int(input('Ano de contratação: '))
    funcionario['salario']=float(input('Salário: R$ '))
    funcionario['aposentadoria']=(funcionario['contratacao']+35)-funcionario['nascimento']
print('-='*30)
for k, v in funcionario.items():
    print(f'- {k} tem o valor {v}')


