#!/bin/usr/python3

from pymongo import MongoClient, DESCENDING #traz o ultimo registro primeiro (ordem descendente)
import time
try:
    client = MongoClient() #conexão com o Mongo Local não precisa passar nenhuma string de conexão
    db = client['chat']
except Exception as e:
    print('ERRO: {}'.format(e))
    exit()

def cadastrar(name, mensagem):
    date = {
        'nome': name,   #Cria um dicionario para armazenar o s dados inputados
        'mensagem1': mensagem,
        'hora': time.strftime('%d-%m-%Y %H:%M:%S')
    }
    db.chat.insert(date) #guarda todo os dados digitados no banco

def ler_msg(): #pegar o ultimo registro no banco e verificar se entrou uma msg nova, pois sempre que alguem digitar uma mensagem deverá ser armazenando no banco de dados
    ultimo = [x for x in db.chat.find().sort('_id', DESCENDING)] #ordenação do ID pelo ultimo registro é o que volta nessa busca
    while True:  #loop infinito para a inserção das novas mensagens
        date = [x for x in db.chat.find().sort('_id', DESCENDING)]
        if date != ultimo: #validação para ver se a data da msg é igual ou diferente, se for diferente executa os proximos passos loops infinito
            ultimo = date
            print('[{}] {} : {} \n'.format(
                date[0]['hora'], date[0]['nome'], date[0]['mensagem1']))
        time.sleep(2) # a cada 2 segundos faz a verificação