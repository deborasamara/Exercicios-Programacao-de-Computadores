"""Escreva um programa que leia 2 valores reais x e y, que devem representar as coordenadas de um ponto em um plano cartesiano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).


Input
A entrada contém uma única linha, com as coordenadas x e y ( - 109 ≤ x, y ≤ 109) do ponto.

Output
A saída deve apresentar o quadrante em que o ponto se encontra: 'Q1', 'Q2', 'Q3' ou 'Q4'.

Se o ponto estiver na origem, escreva a mensagem "Origem".

Se o ponto estiver sobre um dos eixos escreva "Eixo X" ou "Eixo Y", conforme for a situação."""

x, y = map(float, input().split())

if(x==0):
    if(y==0):
        print("Origem")
    else:
        print("Eixo Y")
else:
    if(y==0):
        print("Eixo X")
    else:
        if(y>0):
            if(x>0):
                print("Q1")
            else:
                print("Q2")
        else:
            if (x<0):
                print("Q3")
            else:
                print("Q4")
