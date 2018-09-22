#!/usr/bin/python3 - declaração de todas as bilbiotecas abaixo que serão utilizadas 
from sqlalchemy import update
from core import user_table, engine

con = engine.connect()

atualizar = update(user_table).where(user_table.c.nome == 'vanice souza') #sintaxe da funcao where....onde c indica coluna

commit = atualizar.values(nome= 'juliana souza')
result = con.execute(commit)
print(result.rowcount)
