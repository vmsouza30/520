#!/usr/bin/python3
#llambda para fazer expressoes matematicas - fazer um loop para um range de 10x e armazenar em uma lista
# com o Map faz tudo na mesma linha a sintaxe
#!/usr/bin/python3
#llambda para fazer expressoes matematicas

def soma (x,y):
    return x + y

a = lambda x: x ** 2

nomes = ['vanice', 'juliana']
print(list(map(lambda x: x.title(), nomes)))
print(list(map(lambda y: y ** 2, range(1,11))))

# exemplo de sintase:
# map(lambda x: x if condicao else lambda y: y, sequencia) #sintaxe da formula (tem que fazer a condição)
#sintaxe do IF -> verdade if condição falso
#exemplo: da sintaxe if
[x for x in range(10) if x % 2 == 0]

