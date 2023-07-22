"""Ana e suas amigas estão fazendo um trabalho de geometria para o colégio, em que precisam formar vários triângulos, numa cartolina, com algumas varetas de comprimentos diferentes. Logo elas perceberam que não dá para formar triângulos com três varetas de comprimentos quaisquer: se uma das varetas for muito grande em relação às outras duas, não dá para formar o triângulo.

Neste problema, você precisa ajudar Ana e suas amigas a determinar se, dados os comprimentos de quatro varetas, é ou não é possível selecionar três varetas, dentre as quatro, e formar um triângulo.

Input
A entrada é composta por apenas uma linha contendo quatro números inteiros A, B, C e D (1≤ A,B, C, D ≤ 100).

Output
Seu programa deve produzir apenas uma linha contendo apenas um caractere, que deve ser 'S' caso seja possível formar o triângulo, ou 'N' caso não seja possível formar o triângulo."""

n1, n2, n3, n4 = map(int, input().split())

#Consinderar a Condição de Existência de Triângulos

"Dados três segmentos de reta distintos, se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo."

if (n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1):
    print("S")

elif(n1 + n2 > n4 and n1 + n4 > n2 and n2 + n4 > n1):
    print("S")

elif(n1 + n3 > n4 and n1 + n4 > n3 and  n4 + n3 > n1):
    print("S")

elif(n4 + n2 > n3 and n2 + n3 > n4 and n3 + n4 > n2):
    print("S")

else:
    print("N")