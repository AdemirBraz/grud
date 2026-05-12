def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError,TypeError):
            print('ERRO::DIGITE UM NUMERO REAL VALIDO')    
        except Exception as erro:
            print(erro.__cause__)
        except KeyboardInterrupt:
            print('O USUARIO NAO QUIS INFORMAR O ERRO !')
        else:
            return n
def linha():
    print('-'*30)
def cabeçalho(txt):
    linha()
    print(f'{txt:^30}')
    linha()
def menu(lista):
    cabeçalho('MENU DE CADASTRO')
    for c,items in enumerate(lista, start=1):
        print(f'{c}-{items}') 
    linha()
    opc=leiaint('SUA OPÇÃO: ')
    return opc