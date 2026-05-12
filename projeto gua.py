from time import sleep
from idade.gordo import arquivoexiste
from idade.gordo import criararq
from idade.gordo import lerarq
from idade.gordo import cadastrar   
from menu.menu1 import cabeçalho
from menu.menu1 import leiaint
from menu.menu1 import linha
from menu.menu1 import menu
from idade.gordo import excluir
arq = 'arquivo.txt'
if not arquivoexiste(arq):
    criararq(arq)

while True:
    opcao=menu(['ver pessoas cadastradas','cadastrar nova pessoa','excluir pessoa','sair do programa'])
    linha()
    match opcao:
        case 1:
            lerarq(arq)
            sleep(1)
            continue
        case 2:
            cabeçalho('novo cadastro')
            nome=str(input('nome: ')) 
            idade1=leiaint('Idade: ')
            cadastrar(arq,nome,idade1)
            sleep(1) 
            continue
        case 3:
            cabeçalho('EXCLUIR CADASTRO')
            excluir(arq)
            sleep(1)
            continue
        case 4:
            cabeçalho('seu programa acabou')
            break   
        case _:
            print('erro digite uma opção valida')
            sleep(1)