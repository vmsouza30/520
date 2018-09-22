from flask import Flask, jsonify
from datetime import datetime
from pymongo import MongoClient
import psycopg2

app = Flask(__name__)
# Conexao com mongodb
client = MongoClient()
db = client['projeto']

# Conexao com postgresql
con = psycopg2.connect(
    'host=127.0.0.1 dbname=fundamentals user=admin password=4linux')
cur = con.cursor()


@app.route('/postgresql')
def postgres():
    cur.execute("select * from usuarios;")
    date = cur.fetchall()
    lista = []
    for x in date:
        aux = {"_id": x[0], "nome": x[1], "idade": x[2]}
        lista.append(aux)

    return jsonify(lista)


@app.route('/mongo')
def index():
    lista = []
    for x in db.usuarios.find():
        lista.append(x)
    return jsonify(lista)


@app.route('/login')
def login():
    return jsonify({'mensagem': 'Minha primeira api rest',
                    'data': datetime.now().strftime(
                        '%d-%b-%Y %H:%M:%S')})
   

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

    
    # para rodar a aplicação no prompt
    #digitar pip3 install flask e depois ir para o browser firefox
    # e digitar:

    # http://127.0.0.1:5000/mongo
    # http://127.0.0.1:5000/postgresql