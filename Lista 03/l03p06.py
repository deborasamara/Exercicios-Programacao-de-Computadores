"""Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

Código	Produto	Preço
1	Cachorro-quente	R$ 4,00
2	X-salada	R$ 4,50
3	X-Bacon	R$ 5,00
4	Torrada simples	R$ 2,00
5	Refrigerante	R$ 1,50
Input
A entrada contém dois valores inteiros c (1 ≤ c ≤ 5) e q (1 ≤ q ≤ 100), correspondentes ao código e à quantidade de um item conforme tabela acima.

Output
A saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
"""

escolha, qtd = map(int, input().split())

if(escolha==1):
    total = 4*qtd

if(escolha==2):
    total = 4.50*qtd

if(escolha==3):
    total = 5*qtd

if(escolha==4):
    total = 2*qtd

if(escolha==5):
    total = 1.50*qtd

print("Total: R$", "{:.2f}".format(total))
