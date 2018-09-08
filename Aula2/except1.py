#!/usr/bin/python3
#teste de erro para digitação fora do tipo da lista
convidados = ['vanice','juliana','renata'] # cria a lista
try:
     pos = int(input('Digite a posição do convidado:  '))
     print = (convidados[pos])
except ValueError as value:
    print('Digite somente numeros{}  '.format(value))
    exit()
except NameError as name:
    print('Digite somente {}  '.format(name))
    exit()
except IndexError as index:
    print('Digite a posição {}  '.format(index))
    exit()


        




