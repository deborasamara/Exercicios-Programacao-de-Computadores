"""Escreva um programa que leia um número natural n e informe se o mesmo é primo.

Input
A entrada é composta de uma única linha contendo um número inteiro n (1 ≤ n ≤ 106).

Output
Seu programa deve mostra, em uma linha, a palavra 'Sim' se o n for primo ou 'Nao' (observe que a palavra não está sem o til) caso contrário."""

n = int(input())

qtd_divisores = 0

for i in range(1, n+1):
    if(n % i == 0):
        qtd_divisores = qtd_divisores + 1

if(qtd_divisores == 2):
    print("Sim")

else:
    print("Nao")