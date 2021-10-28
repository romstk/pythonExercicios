def notas(*notas, sit=False):
    """ -> Função que recebe notas calculando a média e a situação do aluno
    :param notas: Uma ou mais notas
    :param sit: Valor opcional, se informado True vai mostrar no resultado a situação do aluno.
    :return: Retorna um dicionário com os dados da maior e menor notas, média e situação do aluno.
    """
    boletim= dict()
    maior=menor=0
    for i, v in enumerate(notas):
        if i == 0:
            maior=v
            menor=v
        else:
            if v>maior:
               maior=v
            if v<menor:
               menor=v
    boletim['quantidade']=len(notas)
    boletim['maiornota']=maior
    boletim['menornota']=menor
    boletim['media']=(sum(notas)/len(notas))
    if sit:
        if boletim['media']>8:
            boletim['Situação']='APROVADO'
        elif boletim['media']<6:
            boletim['Situação']='REPROVADO'
        else:
            boletim['Situação'] = 'RECUPERAÇÃO'
    return boletim


boletim = notas(2,4.43,5,6,7, sit=True)
print(f'{boletim}')