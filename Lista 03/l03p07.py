"""Escreva um programa que leia 2 números inteiros e informe se o maior é múltiplo do menor.

Input
A entrada é composta de dois números inteiros a eb (1 ≤ a, b ≤ 109), cada um em uma linha.

Output
A saída deve conter uma única linha com o texto "Multiplos" caso o maior seja múltiplo do menor ou "Nao multiplos" caso contrário. Observe que não há acentos no texto."""

num1 = int(input())
num2 = int(input())

if(num1>num2):
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1


if(maior%menor==0):
    print("Multiplos")

else:
    print("Nao multiplos")