#!/usr/bin/python3 - declaração de todas as bilbiotecas abaixo que serão utilizadas 
from sqlalchemy import update
from core import user_table, engine

con = engine.connect()

atualizar = update(user_table).where(user_table.c.nome == 'vanice') #buscar quem deseja alterar

atualizar = atualizar.values(nome= 'vanice souza') #quero trocar nome....se quiser outro campo so colocar o nome que está na tabela
result = con.execute(atualizar)
print(result.rowcount)
