#!/usr/bin/python3
#ler um arquivo e retornar a função 
def ler_arquivo(arquivo:str)-> int:
    '''funcao para ler arquivo'''
    conteudo = [] # a variavel recebe vazio [] e junta todos os arquivos em um unico print na tela
    for x in arquivo:
        with open(x, 'r')as arq:
            conteudo += arq.readlines()
    return conteudo #retorna uma lista

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