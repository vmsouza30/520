#!/usr/bin/python3
from pymongo import MongoClient
from pprint import pprint

try:
    client = MongoClient()
    db = client['projeto']

except Exception as e:
    print('Erro:{}'.format(e))
    exit()

ling = {'vanice' : 'python', 'juliana' : 'power bi' , 'renata' : 'sportfire'} #dicionario qualquer exemplo

db.teste.insert(ling)
pprint(db.usuarios.find_one()) # retorna a primeira linha do banco


