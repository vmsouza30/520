#!/usr/bin/python3
#Criar range de letras alfabeticas de A a Z os numeros 97 e 123 são convertidos pelo chr para as letras (Caracter - char)
letras = []
for i in range (97, 123):
    letras.append(chr(i)) # append to our_list

while letras:       #fazer fazer o loop até encontrar o que for letra e armazenar
    print(letras.pop(0))   #pop (0) removendo o espaço que não for letra da letra z p/ a

print(letras) # Print fora do FOR do laço para guardar o resultado, senao fica em Loop"