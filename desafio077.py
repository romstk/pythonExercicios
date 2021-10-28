palavras = ('arvore',
            'casa',
            'carro',
            'parada',
            'hospital',
            'imobiliaria',
            'faca',
            'comida')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos vogais ', end='')
    for letra in palavra:
        if letra in 'aeiouAEIOU':
            print(letra,end='')
