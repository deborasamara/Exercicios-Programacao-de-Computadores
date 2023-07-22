"""Escreva um programa que leia dois números inteiros a e b e mostre todos os múltiplos de a menores ou iguais a b.

Input
Uma única linha com 2 números inteiros a e b (1≤a≤b≤106) separados por um espaço.

Output
Uma única linha com os múltiplos de a, separados por espaço."""

a, b = map(int, input().split())

m_a = []

for i in range(1, b+1):
    if(a*i <= b):
        m_a.append(a*i)

print(*m_a)