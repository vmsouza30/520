#!/usr/bin/python3
#
def pessoas(*nomes):   # transforma em um tupla
    for x in nomes:
         print(x)

def cadastro (**kwargs):  #transforma em um dicionário
    print(kwargs['nome']) #nchama um campo do dicionario cadastro

pessoas('vanice', 'juliana', 'renata')    
cadastro(nome ='joao', sobrenome='souza', idade=30)