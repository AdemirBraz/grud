from menu import menu1
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
    menu1.cabeçalho('PESSOAS CADASTRADAS')
    try:
        with open(nome, 'r') as arquivo:
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
    with open(arq, 'r') as a:
        return a.readlines()
 
 
def _salvar_linhas(arq, linhas):
    with open(arq, 'w') as a:
        a.writelines(linhas)
 
 
def _mostrar_lista(linhas, titulo):
    menu1.cabeçalho(titulo)
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
    idx = menu1.leiaint('Número do cadastro a editar: ') - 1
 
    if 0 <= idx < len(linhas):
        nome = input('Novo nome: ')
        idade = menu1.leiaint('Nova idade: ')
        linhas[idx] = f'{nome};{idade}\n'
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
    idx = menu1.leiaint('Número do cadastro a excluir: ') - 1
 
    if 0 <= idx < len(linhas):
        del linhas[idx]
        _salvar_linhas(arq, linhas)
        print('Cadastro excluído com sucesso')
    else:
        print('Número inválido')
