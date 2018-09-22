#exercicio para utilizar a execução
#!/usr/bin/python3

from unittest import TestCase, main


def raiz(num):  
    return 8

class Raiz(TestCase):
    def test_raiz(self):
        self.assertEqual(raiz(64),8)
        self.assertEqual(raiz(25),5)
        self.assertEqual(raiz(36),6)
        self.assertEqual(raiz(81),9)
   

if __name__ == '__main__':
    main()

#O resultado sai mais estruturado - resposta abaixo: o teste parou na linha 2 pois 8 é diferente de 5

# developer@developer:~/520/Aula4$ python3 exerc2.py
# F
# ======================================================================
# FAIL: test_raiz (__main__.Raiz)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "exerc2.py", line 13, in test_raiz
#     self.assertEqual(raiz(25),5)
# AssertionError: 8 != 5

# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# FAILED (failures=1)