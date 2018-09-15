#!/usr/bin/python3
# extracao de uma conta

class Conta():

    def __init__(self, titular, numero, saldo): # definicao de metodos/parametros para criar um objeto
        self.titular = titular 
        self.numero = numero
        self.saldo = saldo

    def sacar(self, valor): #função sacar
        self.saldo -= valor
        return self.saldo


    def depositar(self, valor): #função depositar
        self.saldo += valor
        return self.saldo

    def transferir(self, valor, conta): #função transferir utuilizar dois parametros o valor a ser transferido e para quem irei transferir
        #tira o valor da minha conta e deposito em outra - chama a classe conta
        self.sacar(valor)
        conta.depositar(valor)

    def __str__(self): 
        return 'titular: {}, numero: {}, saldo: {}'.format(self.titular, self.numero, self.saldo,)     


class Poupanca(Conta): # herança ou seja todos os atributos de conta, poupanca vai ter
     def render_juros(self):
         self.saldo += self.saldo * 0.005
         return self.saldo

     def __str__(self):
         return '{}, {}, {} Poupanca'.format(self.titular, self.numero, self.saldo)

       
conta1 = Conta('Vanice','13520-9',1000) 
conta2 = Poupanca('Juliana','10041-5',1500)

conta2.transferir(100,conta1)
conta2.render_juros()
print(conta1.saldo, conta2.saldo, sep="\n")
