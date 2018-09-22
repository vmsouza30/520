#exercicio para utilizar a execução
#!/usr/bin/python3

from unittest import TestCase, main


def raiz(num): 
    try:  
        return int(num) ** 0.5
    except Exception:
        return False   

class Raiz(TestCase):
    def test_raiz(self):
        self.assertEqual(raiz(64),8)
        self.assertEqual(raiz(25),5)
        self.assertEqual(raiz(36),6)
        self.assertEqual(raiz(81),9)
   

if __name__ == '__main__':
    main()