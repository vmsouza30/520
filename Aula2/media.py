#!/usr/bin/python3
nota1 = int(input('Digite primeira nota1: '))
nota2 = int(input('Digite a segunda nota2: '))

media = (nota1 + nota2) / 2

# media = (faz o calculo direto.
if media >= 7 :
    print ('Aprovado')
elif media <=3 :
    print('Reprovado')
else:
    print('Media')    
    # sempre endentado para funcionar