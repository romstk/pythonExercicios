matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0,3):
    for coluna in range(0,3):
        numero= int(input(f'Informe o número para Matriz posição [{linha} ,{coluna}]  '))
        matriz[linha][coluna]=numero

pares=0
somac=0
maior=0
for linha in range(0,3):
    for coluna in range(0,3):
        # mostra na tela os valores da matriz com 5 espaços centralizado para preencher os números com tamanho 5 para ficarem alinhados
        valor=matriz[linha][coluna]
        #soma os valores pares
        if(valor%2==0):
           pares+=valor
        #soma os valores da terceira coluna
        if(coluna==2):
            somac+=valor
        #maior valor da segunda linha
        if(linha==1):
            if(valor>maior):
               maior=valor

        print(f'[{matriz[linha][coluna]:^5}]',end='')
    print()

print('Analise da matriz:')
print(f'Soma dos valores pares {pares}')
print(f'Soma dos valores da terceira coluna {somac}')
print(f'Maior valor da segunda linha {maior}')
