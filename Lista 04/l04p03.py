"""Escreva um programa que leia 5 números e mostre o maior dos 5.

Input
A entrada é composta de 3 números inteiros a, b, c, d e e (-10000≤ a,b,c,d,e≤10000), cada número em uma linha.

Output
A saída deve conter uma única linha com um número inteiro, o maior dos 5 números lidos."""

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

lista = [n1, n2, n3, n4, n5]

print(max(lista))
