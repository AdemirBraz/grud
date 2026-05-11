from time import sleep
from idade import gordo
from menu import menu1
import menu
arq = 'arquivo.txt'
if not gordo.arquivoexiste(arq):
    gordo.criararq(arq)

while True:
    opcao=menu1.menu(['ver pessoas cadastradas','cadastrar nova pessoa','sair do programa'])
    menu1.linha()
    match opcao:
        case 1:
            gordo.lerarq(arq)
            sleep(1)
            continue
        case 2:
            menu1.cabeçalho('novo cadastro')
            nome=str(input('nome: ')) 
            idade1=menu1.leiaint('Idade: ')
            gordo.cadastrar(arq,nome,idade1)
            sleep(1) 
            continue
        case 3:
            menu1.cabeçalho('seu programa acabou')
            break   
        case _:
            print('erro digite uma opção valida')
            sleep(1)