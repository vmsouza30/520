#!/usr/bin/python3
nota1 = int(input('Digite primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
if media >= 7 :
    print ('media {} Aprovado'.format(media))
elif ((nota1+nota2)/2) <=3 :
    print(('media {} Recuperacao'.format(media))
else:
    print('media {} Reprovado'.format(media))