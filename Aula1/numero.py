#!/usr/bin/python3
nota1 = float(input('Digite primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
# media = (nota1+nota2)/2 para criar a variavel ou coloca a formula no IF
if ((nota1+nota2)/2) >= 7 :
    print ('Aprovado')
elif ((nota1+nota2)/2) <=3 :
    print('Reprovado')
else:
    print('Media')    
    # sempre endentado para funcionar


