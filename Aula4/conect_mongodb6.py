#!/usr/bin/python3 - declaração de todas as bilbiotecas abaixo que serão utilizadas
from pymongo import MongoClient
from pprint import pprint
from bson import ObjectId
from faker import Faker
from datetime import datetime

try:
    client = MongoClient()
    db = client['projeto']

except Exception as e:
    print('Erro:{}'.format(e))
    exit()

print(datetime.now().strftime('%d-%m-%Y %H:$M:%S'))
fake = Faker('pt-BR') # biblioteca que pode inserir aleatorio varios campos

for x in range(10): # inserir 1000 registro aleatórios para criar um arquivo
    registro = {"nome": fake.name(), "cpf": fake.cpf(), "end": fake.address()} #dicionarios com informações aleatorias
    db.pessoas.insert(registro)
    print(registro)

print(datetime.now().strftime('%d-%m-%Y %H:$M:%S'))    