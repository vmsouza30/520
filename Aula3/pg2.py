import psycopg2

try:
    con = psycopg2.connect('host=localhost, dbname=fundamentals user=admin password=4linux1')
except Exception as e:
    print("Erro:{}".format(e))
    exit()
    
    #execução
    # developer@developer:~/520$ . venv/bin/activate
    # (venv) developer@developer:~/520$ cd Aula3
     #(venv) developer@developer:~/520/Aula3$ python3 pg2.py
          #irá dar o erro devido ao editor as vezes não reconhecer os import, executar para ver se não da erro.

