#!/usr/bin/python3
# Print apenas os numeros pares (dica divida tudo por 2 e trabalhar com o resultado da formula de divisao)
numeros = [1,5,4,7,9,10,3000,760] # população da lista de numeros
lista = [] #declarar lista nova para armazenar o resultado desejado.
for i in numeros:
    if i % 2 == 0 :
       lista.append(i) # append to our_list   armazena apenas os numeros pares

print(lista) # Print fora do FOR do laço para guardar o resultado, senao fica em Loop"

#Outra solução lista de compreensão concatenando tudo numa única lista com for e if...mais complexo
# #!/usr/bin/python3
# # Print apenas os numeros pares (dica divida tudo por 2 e trabalhar com o resultado da formula de divisao)
# numeros = [1,5,4,7,9,10,3000,760] # população da lista de numeros
#Lista de compreensao
# lista = [i for i in numeros if x % 2 == 0]
# print(lista)
