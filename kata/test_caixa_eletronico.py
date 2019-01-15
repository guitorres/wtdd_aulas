# coding=utf8
"""
Este problema foi utilizado em 709 Dojo(s).

Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:

Entregar o menor número de notas;
É possível sacar o valor solicitado com as notas disponíveis;
Saldo do cliente infinito;
Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00

Exemplos:

Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.
"""

import unittest

def sacar(valor):
    notas_disponiveis = [100, 50, 20, 10]
    copia_valor = valor
    saque = []
    while (sum(saque) != valor):
        for nota in notas_disponiveis:
            if nota <= copia_valor:
                copia_valor = copia_valor - nota
                saque.append(nota)
                break
    return saque

class CaixaEletronicoTest(unittest.TestCase):
    def test_saca_30(self):
        self.assertEqual([20, 10], sacar(30))

    def test_saca_80(self):
        self.assertEqual([50, 20, 10], sacar(80))

    def test_saca_140(self):
        self.assertEqual([100, 20, 20], sacar(140))


if __name__ == '__main__':
    unittest.main()