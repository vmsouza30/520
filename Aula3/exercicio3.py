#!/usr/bin/python3
# Orientacao a objeto - metodo construtor caracteristica = atributo (sem ' ') e   comportamento = metodo (' ')

class Dog():
    def __init__(self, nome, idade, raca): # definicao de metodos/parametros para criar um objeto
        self.nome = nome
        self.idade = idade
        self.raca = raca

dog1 = Dog('bily',2,'pitbull') #atributos do objeto
dog2 = Dog('xuxo', 5, 'poddle')

print(dog1.nome) # mostrar o resultado

    