"""Escreva um programa que leia um número inteiro N e mostre a tabuada de multiplicação de N.

A tabuada de multiplicação consiste no resultado da multiplicação d N por todos os números entre 1 e 10 (Veja o exemplo de entrada e saída do problema).

Input
A entrada é composta de uma única linha contendo um inteiro N (1≤N≤1000).

Output
Seu programa deve mostrar o a tabuada de N, contendo um cálculo por linha, na forma x N = z, onde x contém todos os números inteiros entre 1 e 10, inclusive, e z é o resultado da multiplicação."""

n = int(input())

for i in range(1, 11):
    print (i,"x",n,"=", n*i)

