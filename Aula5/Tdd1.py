#!/usr/bin/python3
#desenvolvimento orientado a teste....
from unittest import TestCase, main

def eh_impar(num):
    ''' Funcao para validar se um numero é impar. Caso o parametro seja uma string converter para inteiro se nao for possivel retornar None
    '''
    try:
        return True if int(num) %2 != 0 else False #ja verifica se é impar ou par
    except Exception:
        return None

class Impar(TestCase):
    def test_impar(self):
        self.assertEqual(eh_impar(4), False)
        self.assertEqual(eh_impar(9), True)
        self.assertEqual(eh_impar('1234'), False)
        self.assertEqual(eh_impar('12823'), True)
        self.assertEqual(eh_impar('sdada'), None)

if __name__ == '__main__':
    main()
