def ajuda(comando):
    print(f'\033[7;30;46mAcessando o manual do comando {comando}')
    help(comando)
    print('\033[m')


while True:
    print('\033[7;30;42m=-'*15)
    print('Sistema de Ajuda PyHelp ')
    print('=-'*15)
    pesquisa = ajuda(input('\033[mQual o comando que deseja pesquisar ? '))

    resp=str(input('Pesquisar outro? S/N  ')).strip().upper()[0]
    while True:
        if resp not in 'SN':
            resp= print('Opção inválida. Informe S/N  ')
        else:
            break

    if resp=='N':
        break

