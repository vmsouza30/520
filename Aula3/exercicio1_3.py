#!/usr/bin/python3
#ler um arquivo e retornar em forma de lista
def ler_arquivo(arquivo):
    with open(arquivo, 'r') as arq:
        return arq.readlines()
      

a = ler_arquivo('/home/developer/520/Aula2/nomes.txt')     
print(a) 


