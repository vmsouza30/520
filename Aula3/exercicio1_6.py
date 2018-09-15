#!/usr/bin/python3
#ler um arquivo e retornar a função 
def ler_arquivo(arquivo:str)-> int:
    '''funcao para ler arquivo'''
    with open(arquivo, 'r')as arq:
        return arq.readlines() #retorna uma lista

def escrever_arquivo(arquivo:str, conteudo:list):
    '''funcao para escrever no arquivo'''
    conteudo = [x+'\n' for x in conteudo]
    try:
        with open(arquivo, 'a') as arq:
            arq.writelines(conteudo)
    except Exception as e:
        print('Erro: {}'.format(e))

def contar_linhas(arquivo):
    return len(ler_arquivo(arquivo))
    
a = ler_arquivo('/home/developer/520/Aula2/nomes.txt')     
print(a)  