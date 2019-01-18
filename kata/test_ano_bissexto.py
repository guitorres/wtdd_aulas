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

class Ano():
    def __init__(self, ano):
        self.ano = ano


    def _divisivel(self, por):
        return self.ano % por == 0


    def bissexto(self):
        return self._divisivel(4) and (not self._divisivel(100) or self._divisivel(400))


class TestAnoBissexto(unittest.TestCase):
    def test_bissexto(self):
        anos = [1600, 1732, 1888, 1944, 2008]
        for ano in anos:
            self.assertTrue(Ano(ano).bissexto())


    def test_not_bissexto(self):
        anos = [1742, 1889, 1951, 2011]
        for ano in anos:
            print(Ano(ano).bissexto())
            self.assertFalse(Ano(ano).bissexto())


if __name__ == '__main__':
    unittest.main()