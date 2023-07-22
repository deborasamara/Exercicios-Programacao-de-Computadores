"""Escreva um programa que leia N números inteiros e calcule a média dos números lidos. Depois o programa deve contar quantos números estão acima da média e quantos estação abaixo da média.

Input
A entrada é composta de 2 (duas) linhas, a primeira linha contém um inteiro N (1≤N≤106), a quantidade de números a serem lidos. A segunda contém N números inteiros Ai (0≤Ai≤109), separados por espaço.

Output
Seu programa deve imprimir deve imprimir 3 (três) linhas, onde a primeira linha contém um a média dos números lidos, com 1 (uma) casa decimal. A segunda linha contém a quantidade de números abaixo da média e a terceira linha a quantidade de números igual à média ou acima da média."""

n = int(input())
lista = list(map(int, input().split()))

media = sum(lista)/len(lista)

qtd_num_abaixo = 0
qtd_num_maior_ou_igual = 0

for i in range(0, n):
    if(lista[i]<media):
        qtd_num_abaixo = qtd_num_abaixo + 1
    else:
        qtd_num_maior_ou_igual = qtd_num_maior_ou_igual + 1

print(f'{media:.1f}')
print(qtd_num_abaixo)
print(qtd_num_maior_ou_igual)
