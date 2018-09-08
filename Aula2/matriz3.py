#mais elaborado retira o contator
#!/usr/bin/python3
matriz = [
       [1,2,3],
       [4,5,6],
       [7,8,9]
]
a = 0
b = 0

for cont,x in enumerate(matriz):
    a += x[cont]
    b += x[-(cont+1)]
print(a+b)