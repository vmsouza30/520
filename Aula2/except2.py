#!/usr/bin/python3
#teste de erro para digitação fora do tipo da lista
convidados = ['vanice','juliana','renata'] # cria a lista
try:
    pos = int(input('Digite a posição do convidado:  '))
    print = (convidados[pos -1])
except ValueError:
    print('Digite somente numeros')
except IndexError:
    print('a lista tem {} convidados'.format(len(convidados)))



        




