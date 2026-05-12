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
        with open(nome, 'r') as a:
            for linha in a:
                nome_p, idade = linha.strip().split(';')
                print(f'{nome_p:<20}  {idade:>3} Anos')
    except Exception as e:
        print(f'Erro ao ler arquivo: {e}')
        
def cadastrar(arq,nome='DESCONHECIDO',idade=0):
    try:
        a=open(arq,'at')
    except:
        print('ERRO AO CADASTRAR')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO AO CRIAR CADASTRO')
        else:
            print(f'Cadastro Do {nome},Criado Com Sucesso')
            a.close
    return cadastrar    
def editar(arq):
    try:
        with open(arq,'rt') as a:
            linhas=a.readlines()
    except:
        print('ERRO AO EDITAR O ARQUIVO')
    else:
        menu1.cabeçalho('EDITAR CADASTRO')
        for c,linha in enumerate(linhas, start=1):
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n','')
            print(f'[{c}] - {dado[0]}  {dado[1]} Anos')
        editor=int(input('digite o numero do cadastro que deseja editar: '))
        if 1 <= editor <= len(linhas):
            nome=str(input('novo nome: '))
            idade=menu1.leiaint('nova idade: ')    
            linhas[editor-1]=f'{nome};{idade}\n'        
        try:            
            with open(arq,'wt') as a:
                a.writelines(linhas)
        except:
            print('ERRO AO EDITAR O ARQUIVO') 
        else:
            print('cadastro editado com sucesso')
def excluir(arq):
    try:
        with open(arq,'rt') as a:
            linhas=a.readlines()
    except:
        print('erro ao ler arquivo')
    else:
        menu1.cabeçalho('EXCLUIR CADASTRO')
        for c,linha in enumerate(linhas, start=1):
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n',' ')
            print(f'{c} - {dado[0]:<20}  {dado[1]:>3} Anos') 
        excluir=int(input('digite o numero que deseja excluir: '))   
        if 1 <= excluir <= len(linhas):
            del linhas[excluir-1]
            with open(arq,'wt') as a:
                a.writelines(linhas)
            print('cadastro excluido com sucesso')
        else:
            print('numero invalido')              
    finally:
        a.close()
