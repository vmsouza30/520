#!/usr/bin/python3
#teste de erro para digitação fora do tipo da lista
try:
    ling = input('Qual a melhor linguem de prgramacao')
    if ling.lower().strip() != 'python':
        raise ValueError("liguagem errada!")
except ValueError as e:
    print(e)        
