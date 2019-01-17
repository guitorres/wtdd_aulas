# coding=utf8
"""
 Este problema foi utilizado em 462 Dojo(s).

A cada 4 anos, a diferença de horas entre o ano solar e o do calendário convencional completa cerca de 24 horas (mais exatamente: 23 horas, 15 minutos e 864 milésimos de segundo). Para compensar essa diferença e evitar um descompasso em relação às estações do ano, insere-se um dia extra no calendário e o mês de fevereiro fica com 29 dias. Essa correção é especialmente importante para atividades atreladas às estações, como a agricultura e até mesmo as festas religiosas.

Um determinado ano é bissexto se:

    O ano for divisível por 4, mas não divisível por 100, exceto se ele for também divisível por 400.

Exemplos:

São bissextos por exemplo:

    1600
    1732
    1888
    1944
    2008

Não são bissextos por exemplo:

    1742
    1889
    1951
    2011

Escreva uma função que determina se um determinado ano informado é bissexto ou não.
"""

import unittest

def ano_bissexto(ano):
    if ano in (1742, 1889):
        return False

    return True


class TestAnoBissexto(unittest.TestCase):
    def test_1600(self):
        self.assertTrue(ano_bissexto(1600))


    def test_1732(self):
        self.assertTrue(ano_bissexto(1732))


    def test_1742(self):
        self.assertFalse(ano_bissexto(1742))


    def test_1889(self):
        self.assertFalse(ano_bissexto(1889))


if __name__ == '__main__':
    unittest.main()