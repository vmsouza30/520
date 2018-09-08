#!/usr/bin/python3
#primeiro modo ('r' -> read, existem outro w, a, etc...)
#arquivo = open ('nomes.txt','r')
arquivo = open ('nomes.txt','r')
print(arquivo.read())
arquivo.close()