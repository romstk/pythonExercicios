def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada.strip()}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    while True:
        try:
                numero = int(input(msg))
        except (ValueError, TypeError):
                print('\033[1;31mErro. O tipo de dado informado não corresponde a um número inteiro válido.\033[m')
                continue
        except (KeyboardInterrupt):
            print('\033[1;31mErro. O usuário desistiu de digitar.\033[m')
        else:
                return numero
        finally:
                print('Leitura concluída.')


def leiaFloat(msg):
    while True:
        try:
                numero = float(input(msg))
        except (ValueError, TypeError):
                print('\033[1;31mErro. O tipo de dado informado não corresponde a um número float válido.\033[m')
                continue
        except (KeyboardInterrupt):
            print('\033[1;31mErro. O usuário desistiu de digitar.\033[m')
        else:
            return numero
        finally:
                print('Leitura concluída.')

