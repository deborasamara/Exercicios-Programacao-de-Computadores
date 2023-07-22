"""Escreva um programa que leia um número inteiro n e calcule o seguinte somatório:


Input
A entrada é composta de uma única linha, com um valor inteiro n (1 ≤ n ≤ 106).

Output
O programa deve mostra uma linha com o valor do somatório com 4 casas decimais."""


n = int(input())

somatorio = 0

for i in range(1, n+1):
    somatorio = somatorio + (1/i)

print('{:.4f}'.format(somatorio))


