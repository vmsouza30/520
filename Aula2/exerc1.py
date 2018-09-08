#!/usr/bin/python3
#criar uma função que faça o incremento de numero na frente do nome - procedimento para 1 arquivo
#ao inves de criar varios arquivos para fazer essa função, usa-se funcção veja a resolução

#resolução
def numerar_arq(nome):
    with open(nome, 'r') as arquivo: #primeiro le e armazena a lista na variavel conteudo
        conteudo = arquivo.readlines()

    with open(nome, 'w') as arquivo:
        for cont ,x in enumerate(conteudo):
            arquivo.write('{}-{}\n'.format(cont +1, x))

numerar_arq('frutas.txt')

