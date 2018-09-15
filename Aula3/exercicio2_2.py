#!/usr/bin/python3
#llambda para fazer expressoes matematicas - fazer um loop para um range de 10x e armazenar em uma lista

lista = [] 
for x in range(1,11):
    lista.append((lambda y: y ** 2)(x)) 

print(lista)

    

