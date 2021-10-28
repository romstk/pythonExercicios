pessoas = list()
dado = list()

for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade:')))
    #Insera a estrutura de dados chamada dado dentro da list pessoas os dois pontos entre colchete significa que estamos usando o fatiamento de dados, sendo que dois pontos sgignifica todas as posições da estrutura pois não definimos inicio e fim
    pessoas.append(dado[:])
    dado.clear()# limpa a estrutura dao para incluir outros dados dentro do for

for p in pessoas:
    # se a idade é maior ou igual a 21
    if p[1] >=21:
       print(f'{p[0]} é maior de idade.')
    else:
       print(f'{p[0]} é menor de idade.')