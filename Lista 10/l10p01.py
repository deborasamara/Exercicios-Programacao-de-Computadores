"""Uma comunidade indígena produz chinelos de juta e criou um site para vender a produção online. Os chinelos são de apenas um tipo, mas são produzidos em vários tamanhos.

Você foi contratado(a) para desenvolver um programa de controle de estoque para o site. O estoque pode ser visto como uma tabela com uma única linha, em que cada coluna representa um tamanho, como mostrado na figura (a) abaixo. Na figura, os tamanhos são representados por números de 1 a 5. Assim, a tabela da figura (a) informa que o estoque do chinelo de tamanho 1 é 4 unidades, e o estoque do chinelo de tamanho 4 é 3 unidades.


Quando um chinelo é vendido, o estoque deve ser atualizado. Por exemplo, se um chinelo de tamanho 1 for vendido, o estoque atualizado é mostrado na figura (b). Se o estoque para um tamanho de chinelo tem valor zero, chinelos desse tamanho não podem ser vendidos (por exemplo o chinelo de tamanho 3). Ou seja, a venda não é efetivada.

Dados o estoque inicial e a lista de pedidos de clientes, escreva um programa para determinar quantos chinelos são efetivamente vendidos no total. Cada pedido se refere a um único chinelo. As vendas são processadas sequencialmente, na ordem em que os pedidos foram feitos. Se uma venda não é possível por falta de estoque, o pedido correspondente é ignorado.

Input
A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 500), o número de tamanhos de chinelos no estoque. Tamanhos são identificados por inteiros de 1 a N. Cada uma das N linhas seguintes contém N inteiros Xi (0 ≤ Xi ≤ 20), indicando a quantidade de chinelos de tamanho i, para 1 ≤ i ≤ N. A seguir a entrada contém uma linha com um número inteiro P (q ≤ P ≤ 1000), o número de pedidos recebidos pela loja. Cada uma das P linhas seguintes contém um inteiro I representando o tamanho do chinelo de um pedido. Os pedidos são dados na ordem em que foram feitos.

Output
Seu programa deve produzir uma única linha, contendo um único inteiro, o número total de chinelos efetivamente vendidos."""

#quantidade de tamanhos
n_tamanhos = int(input())

#quantidade de cada tamanho
qtd_tamanhos = []
for i in range(n_tamanhos):
    qtd_tamanhos.append(int(input()))

#quantidade de pedidos
n_pedidos = int(input())

#tamanho dos chinelos dos pedidos
pedidos = []
for i in range(n_pedidos):
    pedidos.append(int(input()))

#total chinelos vendidos
vendidos = 0 

for i in range(n_pedidos):
    if(qtd_tamanhos[pedidos[i] - 1] - 1 >= 0):
        vendidos += 1
        qtd_tamanhos[pedidos[i] - 1] = qtd_tamanhos[pedidos[i] - 1] - 1

print(vendidos)



