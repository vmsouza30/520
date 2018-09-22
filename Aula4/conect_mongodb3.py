#!/usr/bin/python3
from pymongo import MongoClient
from pprint import pprint
from bson import ObjectId

try:
    client = MongoClient()
    db = client['projeto']

except Exception as e:
    print('Erro:{}'.format(e))
    exit()

# ling = {'vanice' : 'python', 'juliana' : 'power bi' , 'renata' : 'sportfire'} #dicionario qualquer exemplo

# for x in db.usuarios.find(): # para printar cada select dentro da tabela usuários
#     print(x)
# ou dessa maneira : print([x for in db.usuarios.find()]) #list compreension que tem a lista de dicionarios ou cada registro do banco de dados

db.usuarios.insert({"_id":4, "nome":"jose"}) #inserir
db.usuarios.remove({"_id":4})                       #excluir

# pprint(db.usuarios.find_one()) # retorna a primeira linha do banco