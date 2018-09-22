#!/usr/bin/python3 - declaração de todas as bilbiotecas abaixo que serão utilizadas
from pymongo import MongoClient
from pprint import pprint
from bson import ObjectId
from faker import Faker
from datetime import datetime
from time import sleep

try:
    client = MongoClient()
    db = client['projeto']

except Exception as e:
    print('Erro:{}'.format(e))
    exit()

print(datetime.now().strftime('%d-%m-%Y %H:$M:%S'))
fake = Faker('pt-BR') # biblioteca que pode inserir aleatorio varios campos

for x in db.pessoas.find(): # inserir 1000 registro aleatórios para criar um arquivo
    pprint(x)
    sleep(1)  # para aparecer na tela linha a linha a inserção - chamar a bibliotec from time import sleep


