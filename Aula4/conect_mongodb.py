#!/usr/bin/python3
from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['projeto']
except Exception as e:
    print('Erro:{}'.format(e))


