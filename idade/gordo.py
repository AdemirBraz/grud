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
            dado[1]=dado[1].replace('\n',' ')
            print(f'{dado[0]:<20}  {dado[1]:>3} Anos')    
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
            a.close()   
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
    
