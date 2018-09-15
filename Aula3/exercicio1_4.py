#!/usr/bin/python3
#ler um arquivo e retornar a função para ler varios arquivos, precisa ter os 3 arquivos criados nomes.txt, zzz, xxx
def ler_arquivo(arquivo):
    with open(arquivo, 'r') as arq:
        return arq.readlines().__len__
      

a = ler_arquivo('nomes.txt')  
ler_arquivo('xxx')
ler_arquivo('zzz')
   
   
   
print(a) 