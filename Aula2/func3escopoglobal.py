# #!/usr/bin/python3
# #função que soma dois numeros

# var = 10 #variavel de escopo global

# def escopo():
#     var = 5  #variavel de escopo local
#     print(var)
# escopo() #imprime a variavel local
# print(var) #imprime a variavel global
#exemplo 2
#!/usr/bin/python3

# quando quiser que o valor da global seja alterado colocar global var  (comando global e var é o nome da variavel)

var = 10 #variavel de escopo global

def escopo():
    global var
    var = 5
escopo() #imprime a variavel local
print(var) #imprime a variavel global