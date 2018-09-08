#!/usr/bin/python3
#primeiro modo ('r' -> read, existem outro w, a, etc...) ou dessa maneira utilizando o with open

with open('nomes.txt','a') as arquivo:
     arquivo.write('Segunda\n') #\n escreve na proxima linha
     arquivo.write('Terceira\n') #\n escreve na proxima linha


with open('nomes.txt','a+') as arquivo:
     arquivo.write('Segunda\n') #\n escreve na proxima linha
     arquivo.write('Terceira\n') #\n escreve na proxima linha

