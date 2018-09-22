#exercicio fazer um teste para ver quais as possiveis mensagem de erro que podem ser ocasionadas durante a utilização do usuário no programa

#!/usr/bin/python3
from math import sqrt

def raiz(num):
 #evita o type "error" se for string não passa no primeiro, se for string não passa no segundo - pode se utilizar Try:
    if isinstance(num, int):
        return num ** 0,5
    elif isinstance(num, str) :
        if num.isnumeric():
            return int(num) ** 0,5

assert raiz(64) == 8
assert raiz(25) == 5
assert raiz(81) == 9
assert raiz('36') == 6
assert raiz('dsdfs') == False

