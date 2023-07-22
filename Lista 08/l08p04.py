"""Dado um número inteiro n, encontre o menor número primo maior do que n.

Input
A entrada é composta de uma única linha, contendo um número inteiro n (1 ≤ n ≤ 106).

Output
Seu programa deve mostrar um número inteiro p, que é o menor número primo maior do que n."""




n = int(input())
prox = n + 1

#Mostra a quantidade de divisores
def divisores(prox):
    d = 0 
    for i in range(1, prox + 1):
        if (prox % i == 0):
            d = d + 1
    return d


while (   (divisores(prox)) > 2):
    prox = prox + 1
    (divisores(prox+1))

print(prox)














