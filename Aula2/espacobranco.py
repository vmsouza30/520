#!/usr/bin/python3
#tirar espaço em branco de arquivo, mas não altera o arquivo original, cria uma lista na tela.

with open ('branco.txt','r') as arquivo:
    conteudo = arquivo.readlines()

aux = [] #criar uma lista em branco
for x in conteudo:
    if x == '\n':   
         continue    
    aux.append(x) #armazena os resultados tirando as linhas em branco
print(aux)

#ou pode ser na maneira abaixo como "diferente !=" e retira o continue
#      if x != '\n': 
#          aux.append(x)
