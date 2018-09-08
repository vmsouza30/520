#!/usr/bin/python3

#sintaxe mais facil
# nomes = ['vanice','juliana','renata']
# with open('nomes.txt','a') as arquivo:
#     for nome in nomes:
#          arquivo.write(nomes + '\n')

#ou mais complexo list compreension (lista de compreensão - tudo na mesma linha)

nomes = ['vanice','juliana','renata']
with open('nomes.txt','a') as arquivo:
    arquivo.writelines([x+'\n' for x in nomes])