#!/usr/bin/python3
# Orientacao a objeto - metodo construtor caracteristica = atributo (sem ' ') e   comportamento = metodo (' ')

class Dog():

    def __init__(self, nome, idade, raca): # definicao de metodos/parametros para criar um objeto
        self.nome = nome # atributos
        self.idade = idade
        self.raca = raca
        self.energia = 3

    def latir(self): #função de latir 
        self.energia -= 1 # chama um argumento e altero o valor estabelecido para energia metodo
        print('auauaua')    

    def dormir(self): #função de dormir
        self.energia = 3
        print('Zzzzz') 
    
    def andar(self): #função de andar
        self.energia -= 1
        print('andando') 
    
    def __str__(self): #função de dormir
        return 'nome: {}, idade: {}, raca: {}'.format(self.nome, self.idade, self.raca,)     

dog1 = Dog('bily',2,'pitbull') #atributos do objeto não passo os parenteses
dog2 = Dog('xuxo', 5, 'poddle') 
# print(dir(dog1))
print(dog1)
print(dog1.energia)
dog1.latir()
dog1.andar()
print(dog1.energia)
dog1.__doc__
print(dog2)
print(dog2.energia)
dog1.latir()
dog1.dormir()
print(dog2.energia)
dog2.__doc__

# print(dog1.nome)
# dog1.latir()



