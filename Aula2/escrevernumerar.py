# #!/usr/bin/python3
#o arquivo já tem conteúdo.....não precisa da lista inicial
# #adicionar numeracao na frente do conteudo da lista

# with open('nomes.txt','r') as arquivo: #primeiro le e armazena a lista na variavel conteudo
#     conteudo = arquivo.readlines()

# #percorrer a lista e incluir a formatação na frente (1-....2-)
# with open('nomes1.txt','w') as arquivo:
#     for x in conteudo:
#         print('{}-{}\n'.format(1, x))

#para acrescentar numero sequencial:

with open('nomes.txt','r') as arquivo: #primeiro le e armazena a lista na variavel conteudo
     conteudo = arquivo.readlines()

with open('nomes.txt','w') as arquivo:
    for cont ,x in enumerate(conteudo):
        arquivo.write('{}-{}\n'.format(cont +1, x))