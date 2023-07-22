"""Escreva uma função que receba dois números inteiros, dois pesos, e retorne a média ponderada dos mesmos.

Input
A função recebe como parâmetros 4 (quatro) números inteiros v1, p1, v2 e p2 e (0 ≤ v1, p1, v2, p2 ≤ 106).

Assinatura da função em Python:

def media_ponderada(v1, p1, v2, p2)

Importante: O código que você enviar não deve mostrar nada na tela (função print()). Deve conter apenas a implementação da função.

Output
A função deve retornar um número real, com a média ponderada calculada a partir da fórmula"""

def media_ponderada(v1, p1, v2, p2):
    media = (v1 * p1 + v2*p2)/(p1+p2)
    return media