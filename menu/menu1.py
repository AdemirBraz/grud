def leiaint(msg):
    while True:
        try:
            return int(input(msg))
        except (ValueError, TypeError):
            print('Erro: digite um número válido')
        except KeyboardInterrupt:
            print('\nEntrada cancelada')

def linha():
    print('-'*30)

def cabeçalho(txt):
    linha()
    print(f'{txt:^30}')
    linha()

def menu(opcoes):
    cabeçalho('MENU DE CADASTRO')
    for pos, item in enumerate(opcoes, start=1):
        print(f'{pos} - {item}')
    linha()
    return leiaint('Sua opção: ')