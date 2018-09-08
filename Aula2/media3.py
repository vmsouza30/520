#!/usr/bin/python3
# está validando para entrada de nova até 10, se for maior avisa com erro, e faz a qtdade -1 para tirar da media
# caso queira que force sempre para entrar com um valor correto, utilizar WHILE e tirar   qtdade -1
qtdadenotas = int(input('Digite a quantidade de notas: '))
total = 0
# ou total = float(0)

for x in range(qtdadenotas):
    nota = int(input('Digite a nota{}: '.format(x+1)))
    if nota > 10:
        print ('Nota invalida!')
        qtdadenotas -= 1 # é necessario colocar essa variavel para nao contabilizar na media um valor invalido
        continue
    total += nota
       
media =  total/ qtdadenotas

# media = (faz o calculo direto)
if media >= 7 :
    print (media,'Aprovado')
elif media <=3 :
    print(media,'Reprovado')
else:
    print(media,'Media')    
    # sempre endentado para funcionar