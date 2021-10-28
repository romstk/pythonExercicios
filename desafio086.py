matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0,3):
    for coluna in range(0,3):
        numero= int(input(f'Informe o número para Matriz posição [{linha} ,{coluna}]  '))
        matriz[linha][coluna]=numero

for linha in range(0,3):
    for coluna in range(0,3):
        # mostra na tela os valores da matriz com 5 espaços centralizado para preencher os números com tamanho 5 para ficarem alinhados
        print(f'[{matriz[linha][coluna]:^5}]',end='')
    print()



