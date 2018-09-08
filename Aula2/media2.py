#!/usr/bin/python3

qtdadenotas = int(input('Digite a quantidade de notas: '))
total = 0
# ou total = float(0)

for x in range(qtdadenotas):
    #print('Digite a nota', x+1,':') 
    #nota = float(input())
    # primeira forma é utilizando as duas informações comentadas acima e tirar a proxima NOTA ou executar direto em uma linha, ai só utiliza a linha NOTA
    nota = int(input('Digite a nota {}: '.format(x+1)))
  
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