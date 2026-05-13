from UI import menu_ui
import os

def arquivo_existe(nome):
    return os.path.exists(nome)
    
def criar_arq(nome):
    try:
        open(nome, 'w').close()
        print(f'Arquivo {nome} criado com sucesso')
    except Exception as e:
        print(f'Erro ao criar arquivo: {e}')
               
def ler_arq(nome):
    menu_ui.cabeçalho('PESSOAS CADASTRADAS')
    try:
        with open(nome, 'r') as arquivo:
            conteudo = arquivo.read().strip()
            if not conteudo:
                print('Nenhum cadastro encontrado.')
                return
            for linha in arquivo:
                nome_p, idade = linha.strip().split(';')
                print(f'{nome_p:<20}  {idade:>3} Anos')
    except Exception as e:
        print(f'Erro ao ler arquivo: {e}')
        
def cadastrar(arq, nome='DESCONHECIDO', idade=0):
    try:
        with open(arq, 'a') as arquivo:
            arquivo.write(f'{nome};{idade}\n')
        print(f'Cadastro de {nome} criado com sucesso')
    except Exception as e:
        print(f'Erro ao cadastrar: {e}')

# helpers ------------------------
def _ler_linhas(arq):
    with open(arq, 'r') as arquivo:
        return arquivo.readlines()
 
 
def _salvar_linhas(arq, linhas):
    with open(arq, 'w') as arquivo:
        arquivo.writelines(linhas)
 
 
def _mostrar_lista(linhas, titulo):
    menu_ui.cabeçalho(titulo)
    for i, linha in enumerate(linhas, start=1):
        nome_p, idade = linha.strip().split(';')
        print(f'[{i}] {nome_p:<20}  {idade:>3} Anos')
 
# editar ---------------------------------------
def editar(arq):
    try:
        linhas = _ler_linhas(arq)
    except Exception as e:
        print(f'Erro ao abrir arquivo: {e}')
        return
 
    _mostrar_lista(linhas, 'EDITAR CADASTRO')
    if not linhas:
        print('Nenhum cadastro para editar.')
        return
    idx = menu_ui.leiaint('Número do cadastro a editar: ') - 1 
    if 0 <= idx < len(linhas):
        nome=str(input('Novo nome: ')).strip()
        while not nome or nome.isnumeric() or nome.isspace():
            print('Nome inválido. Tente novamente.')
            nome=str(input('Novo nome: ')).strip()
        idade = menu_ui.leiaint('Nova idade: ')
        while idade < 0 or idade > 120 or not isinstance(idade, int):
            print('Idade Inválida. Tente novamente.')
            idade = menu_ui.leiaint('Nova idade: ')
        linhas[idx] = f'{nome};{idade}\n'
        
        if idade < 0:
            print('Idade não pode ser negativa. Editação cancelada.')
            return
        _salvar_linhas(arq, linhas)
        print('Cadastro editado com sucesso')
    else:
        print('Número inválido')


def excluir(arq):
    try:
        linhas = _ler_linhas(arq)
    except Exception as e:
        print(f'Erro ao abrir arquivo: {e}')
        return
 
    _mostrar_lista(linhas, 'EXCLUIR CADASTRO')
    idx = menu_ui.leiaint('Número do cadastro a excluir: ') - 1
 
    if 0 <= idx < len(linhas):
        del linhas[idx]
        _salvar_linhas(arq, linhas)
        print('Cadastro excluído com sucesso')
    else:
        print('Número inválido')
