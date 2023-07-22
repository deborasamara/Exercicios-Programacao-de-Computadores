"""Escreva um programa que leia 3 números inteiros e mostre o maior.

Input
A entrada é composta de 3 números inteiros a, b e c ( - 10000 ≤ a, b, c ≤ 10000), cada número em uma linha.

Output
A saída deve conter uma única linha com um número inteiro, o maior dos 3 números lidos."""

n1 = int(input())
n2 = int(input())
n3 = int(input())

if(n1>n2):
    if(n1>n2):
        print(n1)
    else:
        print(n2)

else:
    if(n2>n3):
        print(n2)
    else:
        print(n3)

