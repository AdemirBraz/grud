from time import sleep
from idade import gordo
from menu import menu1

ARQ = 'arquivo.txt'

if not gordo.arquivo_existe(ARQ):
    gordo.criar_arq(ARQ)

while True:
    n = menu1.menu([
        'Ver pessoas cadastradas',
        'Cadastrar nova pessoa',
        'Editar cadastro',
        'Excluir cadastro',
        'Sair do programa',
    ])
    menu1.linha()

    match n:
        case 1:
            gordo.ler_arq(ARQ)
        case 2:
            menu1.cabeçalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = menu1.leiaint('Idade: ')
            gordo.cadastrar(ARQ, nome, idade)
        case 3:
            gordo.editar(ARQ)
        case 4:
            gordo.excluir(ARQ)
        case 5:
            menu1.cabeçalho('Programa encerrado')
            break
        case _:
            print('Opção inválida')

    sleep(1)