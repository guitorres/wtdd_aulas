# coding=utf8

"""
Este problema foi utilizado em 374 Dojo(s).

Escreva um programa que gere todos os anagramas potenciais de uma string.

Por exmplo, os anagramas potenciais de "biro" são:

biro bior brio broi boir bori
ibro ibor irbo irob iobr iorb
rbio rboi ribo riob roib robi
obir obri oibr oirb orbi orib

Traduzido de: http://www.cyber-dojo.com/
"""
import unittest

def anagrama(texto):
    result = ['biro', 'bior', 'brio', 'broi', 'boir', 'bori',
              'ibro', 'ibor', 'irbo', 'irob', 'iobr' 'iorb',
              'rbio', 'rboi', 'ribo', 'riob', 'roib' 'robi',
              'obir', 'obri', 'oibr', 'oirb', 'orbi' 'orib']
    result.sort()

    texto_lista = list(texto)
    result = []
    teste = ''
    for pos_original  in range(len(texto_lista)):
        texto_anagrama = []
        for pos_nova in range(len(texto_lista)):
            texto_anagrama = texto_lista[:]
            texto_anagrama[pos_original] = texto_lista[pos_nova]
            texto_anagrama[pos_nova] = texto_lista[pos_original]
            teste = ''.join(texto_anagrama)
            if teste not in result:
                result.append(teste)

    #result.sort()
    return result

def hanagrama(texto):
    import math
    original = anagrama(texto)
    ab = original[:]
    for t in ab:
        vai = anagrama(t)
        for v in vai:
            if v not in original:
                original.append(v)
    #if len(original) != math.factorial(len(texto)):
        #hanagrama()
    return original

class TestAnagramas(unittest.TestCase):
    def test_biro(self):
        expected = ['biro', 'bior', 'brio', 'broi', 'boir', 'bori',
                    'ibro', 'ibor', 'irbo', 'irob', 'iobr' 'iorb',
                    'rbio', 'rboi', 'ribo', 'riob', 'roib' 'robi',
                    'obir', 'obri', 'oibr', 'oirb', 'orbi' 'orib']
        expected.sort()
        #print(anagrama('biro'))
        self.assertListEqual(expected, anagrama('biro'))


if __name__ == '__main__':
    unittest.main()

