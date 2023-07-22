"""Escreva uma função que receba 5 (cinco) números inteiros e retorne o maior dos mesmos.

Input
A função recebe como parâmetros 5 (cinco) números inteiros a, b, c, d e e ( - 1000 ≤ a, b, c, d, e ≤ 1000).

Assinatura da função em Python:

def maior5(a, b, c, d, e)

Importante: O código que você enviar não deve mostrar nada na tela (função print()). Deve conter apenas a implementação da função.

Output
A função deve retornar um valor inteiro, o maior número entre a, b, c, d e e."""

def maior5(a, b, c, d, e):
    l = [a, b, c, d, e]
    return max(l)
