#!/usr/bin/python3 - declaração de todas as bilbiotecas abaixo que serão utilizadas 
from sqlalchemy import insert
from core import user_table, engine # core é o nome do arquivo python criado (core.py)

con = engine.connect()
ins = user_table.insert() #varios metodos...

new = ins.values(idade=39, nome='vanice', senha='teste1234')
con.execute(new)

#ou
# con.execute(user_table.insert(), [
#     {'nome': 'marcio', 'dade':21, 'senha': 'semsenha'},
#     {'nome': 'gustavo', 'dade':18, 'senha': 'abacaxi123'},
#     {'nome': 'guilherme', 'dade':22, 'senha': 'goiaba123'}
#   ])

#ou
# con.execute(ins, [
#     {'nome': 'marcio', 'dade':21, 'senha': 'semsenha'},
#     {'nome': 'gustavo', 'dade':18, 'senha': 'abacaxi123'},
#     {'nome': 'guilherme', 'dade':22, 'senha': 'goiaba123'}
#   ])

