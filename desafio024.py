cidade = str(input('Digite a cidade onde nasceu. O sistema vai apresentar a mensagem True se ela começar com a palavra SANTO  : ')).strip().upper().split()

valida= ('SANTO' in cidade)

print('Cidade informada inicia com a palavra {}'.format(cidade[0]))
print(valida)
