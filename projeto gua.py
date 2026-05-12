from time import sleep
from unittest import case
from idade.gordo import arquivoexiste
from idade.gordo import criararq
from idade.gordo import lerarq
from idade.gordo import cadastrar
from menu.menu1 import menu
from menu.menu1 import linha
from menu.menu1 import cabeçalho
from menu.menu1 import leiaint
from idade.gordo import editar
from idade.gordo import excluir
arq = 'arquivo.txt'
if not arquivoexiste(arq):
    criararq(arq)

while True:
    n=menu(['ver pessoas cadastradas','cadastrar nova pessoa','editar cadastro','excluir cadastro','sair do programa'])
    linha()
    match n:
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
            editar(arq)
            sleep(1)
        case 4:
            excluir(arq)
            sleep(1)
        case 5:
            cabeçalho('seu programa acabou')
            break   
        case _:
            print('erro digite uma opção valida')
            sleep(1)