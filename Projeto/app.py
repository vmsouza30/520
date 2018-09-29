import modulos.banco as banco #deu um apelido  para o "Modulos.banco" - qdo for utilizar no script só usa a palavra banco (alias)
import threading

if __name__ == '__main__':
    user = input('Nickname: ')
    try:
        f = threading.Thread(target=banco.ler_msg)
        f.start()
    except Exception as e:
        print('Falha ao criar thread : {}'.format(e))
    # Enquanto thread rodar em segundo plano
    while f.isAlive:
        msg = input()
        banco.cadastrar(user, msg)