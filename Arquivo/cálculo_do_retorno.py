# -*- coding: utf-8 -*-
"""Cálculo do retorno

O retorno de uma carteira pode ser obtido a partir dos seus retornos individuais. Esses retornos são multiplicados pelas suas respectivas probabilidades e todos os valores somados.

"
"""

r1 = float(input('Retorno do ativo 1: '))
r2 = float(input('Retorno do ativo 2: '))
r3 = float(input('Retorno do ativo 3: '))

p1 = float(input('Probabilidade 1: '))
p2 = float(input('Probabilidade 2: '))
p3 = float(input('Probabilidade 3: '))

ret_medio = r1*p1 + r2*p2 + r3 * p3

print('Retorno médio: ', ret_medio)