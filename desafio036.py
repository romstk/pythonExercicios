print('A seguir informe as variáveis para cálculo do financiamento bancário: ')
casa = float(input('Intorme o valor do imóvel: R$ '))
salario = float(input('Informe o seu salário: R$ '))
prazo = float(input('Informe o prazo do financiamento em anos : '))

parcela = (casa / prazo)/12

if parcela > (salario * 0.30):
    print('A parcela R$ {:.2f} ficou com o valor acima do permitido de 30% sobre o salário.  '.format(parcela))
    print(('Financiamento Não Aprovado. '))
else:
    print(('A parcela R$ {:.2f} ficou de acordo com o máximo permitido.. Financiamento aprovado. ').format(parcela))
    print(('Financiamento Aprovado. '))