#!/usr/bin/python3 - declaração de todas as bilbiotecas abaixo que serão utilizadas 
from sqlalchemy import select
from core import user_table

result = select([user_table]) #seleciona as tabelas que quero fazer um select, join....etc..
result2 = select([user_table]).where(user_table.c.nome == 'vanice')

# for x in result.execute():
#     print(x)

# ou
print([x for x in result2.execute()])

