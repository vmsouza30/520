#mais elaborado retira o contator e cria um única variavel para soma as diagonais
#!/usr/bin/python3
matriz = [
       [1,2,3],
       [4,5,6],
       [7,8,9]
]
soma = 0

for cont,x in enumerate(matriz):
    soma += x[cont]
    soma += x[-(cont+1)]

print(soma)
