def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except(ValueError,TypeError):
            print('EERO::DIGITE UM NUMERO REAL VALIDO')    
        except Exception as erro:
            print(erro.__cause__)
        except KeyboardInterrupt:
            print('O USUSARIO NAO QUIS INFORMAR O ERRO !')
        else:
            return n
def linha():
    print('-'*30)
def cabeçalho(txt):
    linha()
    print(f'{txt:^30}')
    linha()
def menu(lista):
    cabeçalho('menu de cadastro')
    c=1
    for items in lista:
        print(f'{c}-{items}')
        c+=1
    linha()
    opc=leiaint('SUA OPÇÃO: ')
    return opc