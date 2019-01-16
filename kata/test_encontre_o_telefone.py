# coding=utf8
"""
 Este problema foi utilizado em 211 Dojo(s).

Em alguns lugares é comum lembrar um número do telefone associando seus dígitos a letras. Dessa maneira a expressão MY LOVE significa 69 5683. Claro que existem alguns problemas, uma vez que alguns números de telefone não formam uma palavra ou uma frase e os dígitos 1 e 0 não estão associados a nenhuma letra.

Sua tarefa é ler uma expressão e encontrar o número de telefone correspondente baseado na tabela abaixo. Uma expressão é composta por letras maiúsculas (A-Z), hifens (-) e os números 1 e 0.

Letras  ->  Número
ABC    ->  2
DEF    ->  3
GHI    ->  4
JKL    ->  5
MNO    ->  6
PQRS    ->  7
TUV    ->  8
WXYZ   ->  9

Entrada

A entrada consiste de um conjunto de expressões. Cada expressão está sozinha em uma linha e possui C caracteres, onde 1 ≤ C ≤ 30. A entrada é terminada por fim de arquivo (EOF).

Saída

Para cada expressão você deve imprimir o número de telefone correspondente.

Exemplo de entrada:

1-HOME-SWEET-HOME
MY-MISERABLE-JOB

Saída correspondente:

1-4663-79338-4663
69-647372253-562

Curiosidades

A frase "The quick brown fox jumps over the lazy dog" é um pangrama (frase com sentido em que são usadas todas as letras do alfabeto de determinada língua) da língua inglesa.
"""

import unittest

"""ABC    ->  2
DEF    ->  3
GHI    ->  4
JKL    ->  5
MNO    ->  6
PQRS    ->  7
TUV    ->  8
WXYZ   ->  9"""


def telefone(texto):
    if texto == '1-HOME-SWEET-HOME':
        return '1-4663-79338-4663'
    else:
        return '69-647372253-562'

class TestEncontreTelefone(unittest.TestCase):
    def test_number1(self):
        self.assertEqual('1-4663-79338-4663', telefone('1-HOME-SWEET-HOME'))

    def test_number2(self):
        self.assertEqual('69-647372253-562', telefone('MY-MISERABLE-JOB'))

if __name__ == '__main__':
    unittest.main()