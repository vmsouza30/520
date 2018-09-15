#!/usr/bin/python3
# Orientacao a objeto - metodo construtor caracteristica = atributo (sem ' ') e   comportamento = metodo (' ')

class Dog():
    def __init__(self, nome, idade, raca): # definicao de metodos/parametros para criar um objeto
        self.nome = nome
        self.idade = idade
        self.raca = raca
    def latir(self): #função de latir
        print('auauaua')    

    def dormir(self): #função de dormir
        print('Zzzzz')   

dog1 = Dog('bily',2,'pitbull') #atributos do objeto não passo os parenteses
dog2 = Dog('xuxo', 5, 'poddle') 

print(dog1.nome) # mostrar o resultado
dog1.latir() # # metodo () passo os parentese  / estou acionando o objeto latir (the sims4 o cachorro irá latir)