import psycopg2
ip, base, user, senha = 'localhost', 'fundamentals', 'admin', '4linux'

try:
    con = psycopg2.connect('host={} dbname={} user={} password={}'.format(ip, base, user, senha
    ))
except Exception as e:
    print("Erro:{}".format(e))
    exit()

cur = con.cursor() #objeto que irá fazer as operações dentro do banco (delete, select, etc....)
cur.execute("select * from usuarios;")
for x in cur.fetchall(): #lista de tuppla - é acessado por um indice - e ficar organizado com ....
    print('''
    ID: {:.>10}
    Nome: {:.>12}
    Idade: {:.>8} 
    '''.format(x[0], x[1], x[2]))

#outros exemplos de comandos :
#cur.execute("update usuarios set nome='vanice' where id=1;")
#cur.execute("insert into usuarios\ (nome, idade) values ('joana',52);")

con.commit() # para registrar todas as informações no banco obrigatorio

cur.close() #fechar as conexoes com o banco de dados
con.close()

    #execução
    # developer@developer:~/520$ . venv/bin/activate
    # (venv) developer@developer:~/520$ cd Aula3
     #(venv) developer@developer:~/520/Aula3$ python3 pg2_1.py
     #irá dar o erro devido ao editor as vezes não reconhecer os import, executar para ver se não da erro.