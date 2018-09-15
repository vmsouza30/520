#!/usr/bin/python3
#ler um arquivo e retornar a função para ler varios arquivos, precisa ter os 3 arquivos criados nomes.txt, zzz, xxx

def ler_arquivo(arquivo:str)-> int:
    '''funcao para ler arquivo'''
    with open(arquivo, 'r')as arq:
        return arq.readlines()

def escrever_arquivo(arquivo:str, conteudo:list):
    '''funcao para escrever no arquivo'''
    try:
        with open(arquivo, 'a') as arq:
            arq.writelines(conteudo)
    except Exception as e:
        print('Erro: {}'.format(e))

a = ler_arquivo('/home/developer/520/Aula2/nomes.txt')     
print(a)  