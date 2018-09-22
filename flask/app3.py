from flask import Flask, jsonify
from datetime import datetime
from pymongo import MongoClient
import psycopg2
from json import dumps, loads
from bson import ObjectId

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

def serial(dct):
    for k in dct:
        if isinstance(dct[k], ObjectId):
            dct[k] = 'objectid' 
    return dct
    
@app.route('/teste')
def teste():
    return jsonify(([serial(x) for x in db.pessoas.find()]))

#ou - passagem do find com uma procura especifica mais avançada
# @app.route('/teste'/<cpf>)
# def teste(cpf):
#     return jsonify(([serial(x) for x in db.pessoas.find({'CPF:cpf})]))

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
    # http://127.0.0.1:5000/teste
    