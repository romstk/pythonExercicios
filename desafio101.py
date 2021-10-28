def voto(nascimento):
    from datetime import date
    idade = date.today().year-nascimento
    if idade < 16:
        return f'Com idade {idade} anos. Não vota.'
    elif idade >=16 and idade < 18 or idade >65 :
        return f'Com idade {idade} anos. Voto facultativo'
    else:
        return f'Com idade {idade} anos. Voto obrigatório'
print('-'*40)
nascimento = int(input('Informe o ano de seu nascimento: '))
print(voto(nascimento))

