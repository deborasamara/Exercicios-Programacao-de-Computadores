"""Escreva um programa que leia N números inteiros e calcule a média dos números lidos. Depois o programa deve mostrar quantos números estão acima da média e quais são, também deve mostrar quantos estação abaixo da média e quais são.

Input
A entrada é composta de 2 (duas) linhas, a primeira linha contém um inteiro N (1 ≤ N ≤ 106), a quantidade de números a serem lidos. A segunda contém N números inteiros Ai (0 ≤ Ai ≤ 109), separados por espaço.

Output
Seu programa deve imprimir deve imprimir 3 (três) linhas, onde a primeira linha contém um a média dos números lidos, com 1 (uma) casa decimal. A segunda linha contém a quantidade de números abaixo da média e a lista dos números, na ordem em que foram lidos, separados por espaço. Por fim, na terceira e última linha, a quantidade de números igual à média ou acima da média e os números, também separados por espaço."""

n = int(input())
lista = list(map(int, input().split()))

n_acima_m = 0
n_abaixo_m = 0
n_ab = []
n_ac = [] 

media = sum(lista)/n

for i in range(0, n):
    if(lista[i]<media):
        n_abaixo_m =  n_abaixo_m + 1
        n_ab.append(lista[i])

    elif(lista[i]>media):
        n_acima_m = n_acima_m + 1
        n_ac.append(lista[i])

print(f'{media:.1f}')
print(n_abaixo_m, *n_ab)
print(n_acima_m, *n_ac)

