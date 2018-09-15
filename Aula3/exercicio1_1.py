#!/usr/bin/python3
#o que define o argumentos é o simbolo *
def pessoas(*nomes):   # transforma em um tupla
    for x in nomes:
         print(x)

def cadastro (**kwargs):  #transforma em um dicionário
    print(kwargs)

pessoas('vanice', 'juliana', 'renata')    
cadastro(nome ='joao', sobrenome='souza', idade=30)
