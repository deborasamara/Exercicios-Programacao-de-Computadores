"""Escreva um programa que leia um número inteiro n e mostre os divisores de n, incluindo ele mesmo.

Input
A entrada é composta de uma única linha com um inteiro n (1≤n≤106)

Output
Seu programa deve mostrar, em uma única linha, todos os divisores de n, separados por espaços."""

n = int(input())

divisores = []

for i in range(1, n+1):
    if(n % i == 0):
        divisores.append(i)

print(*divisores)
