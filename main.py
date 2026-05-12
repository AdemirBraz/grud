from time import sleep
from repositorio import crud
from UI import menu_ui

ARQ = 'arquivo.txt'

if not crud.arquivo_existe(ARQ):
    crud.criar_arq(ARQ)

while True:
    n = menu_ui.menu([
        'Ver pessoas cadastradas',
        'Cadastrar nova pessoa',
        'Editar cadastro',
        'Excluir cadastro',
        'Sair do programa',
    ])
    menu_ui.linha()

    match n:
        case 1:
            crud.ler_arq(ARQ)
        case 2:
            menu_ui.cabeçalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = menu_ui.leiaint('Idade: ')
            crud.cadastrar(ARQ, nome, idade)
        case 3:
            crud.editar(ARQ)
        case 4:
            crud.excluir(ARQ)
        case 5:
            menu_ui.cabeçalho('Programa encerrado')
            break
        case _:
            print('Opção inválida')

    sleep(1)