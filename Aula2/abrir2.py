#!/usr/bin/python3
#primeiro modo ('r' -> read, existem outro w, a, etc...) ou dessa maneira utilizando o with open

with open('nomes.txt','r') as arquivo:
    print(arquivo.read())
