#!/usr/bin/python3
# importação de uma ou mais classes objetos a partir de outro arquivo 

from exercicio3_6 import Conta,Poupanca #nome do arquivo e as classes que irão subir
       
conta1 = Conta('Vanice','13520-9',1000) 
conta2 = Poupanca('Juliana','10041-5',1500)

conta2.transferir(500,conta1)

print(conta1.saldo, conta2.saldo, sep="\n")


