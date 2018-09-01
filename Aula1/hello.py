#!/usr/bin/python3
nota1 = int(input('Digite primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = (nota1+nota2)/2 
if media >= 7 :
    print ('Media {}, Aprovado'.format(media))
elif media <=3 :
    print ('Media {}, Recuperacao'.format(media))
else:
    print ('Media {}, Reprovado'.format(media))  

