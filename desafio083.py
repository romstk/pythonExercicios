expressao = str(input('Digite uma expressão: '))
pilha = []

#Le toda a string coontendo a expressão
for simbolo in expressao:
    #para cada parentese aberto grava o simbolo na pilha para controle
    if simbolo == '(':
        pilha.append(simbolo)
    else:
        #se a pilha for >0, signigica que ja possui um parentese de abertura, então se contiver um de fechamento exclui o elemento da pilha para ir mantendo o controle de pares.
        if simbolo == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                # Se a lista estiver vazia inclcui o pententese de fechamento na pilha, porém a expressão será constatada inválida pois não fechará os pares.
                pilha.append(')')

if len(pilha)==0:
    print('A expressão é válida')
else:
    print('A expressão é inválida')
