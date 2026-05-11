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
    
