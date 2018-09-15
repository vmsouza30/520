from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Ola mundo!</h1>'

@app.route('/login')
def login():
    return jsonify({'mensagem': 'Minha primera api rest', 'data':datetime.now().strftime('%d-%b-%Y %H:%M:%S')})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

    #.venv/bin/activatepara rodar esse script é necessario no terminal estar dentro da maquina virtual 
    # (venv) developer@developer:~/520/flask
    # . activate
    # python3 app.py
    # para sair <ctrl c >
    #or
    #(venv) developer@developer:~/520/flask
    # 
