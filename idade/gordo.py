from menu import menu1

def arquivoexiste(nome):
    try:
        a=open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criararq(nome):
    try:
        a=open(nome,'wt+')
        a.close()
    except:
        print('erro ao criar arquivo')
    else:
        print(f'Arquivo {nome} crianda com sucesso') 
               
def lerarq(nome):
    try:
        a=open(nome,'rt')
    except:
        print('erro ao ler arquivo')
    else:
        menu1.cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n','')
            print(f'{dado[0]}  {dado[1]} Anos')    
    finally:
        a.close()
        
def cadastrar(arq,nome='DESCONHECIDO',idade=0):
    try:
        a=open(arq,'at')
    except:
        print('ERRO AO CADASTRAR')
    else:
        try:
            a.write(f'{nome};{idade}')
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
              
    finally:
        a.close()
