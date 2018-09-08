#!/usr/bin/python3

qtdadenotas = int(input('Digite a quantidade de notas'))
total = float(0)

for x in range(qtdadenotas):
    nota = float(input('Digite as notas'))
    total += nota
       
media =  total/ qtdadenotas

# media = (faz o calculo direto.
if media >= 7 :
    print (media,'Aprovado')
elif media <=3 :
    print(media,'Reprovado')
else:
    print(media,'Media')    
    # sempre endentado para funcionar