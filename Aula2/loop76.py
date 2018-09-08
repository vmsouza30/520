#Nessa sintaxe  quando o else pertencer ao FOR ir aexecutar a msg final depois que procurar tudo
#!/usr/bin/python3
nomes = ['vanice','juliana','carol']
busca = input('Digite um nome:  ')

for nome in nomes:
    if busca.lower().strip() == nome:
        print('achei')
        break
else:
    print('não achei')      
