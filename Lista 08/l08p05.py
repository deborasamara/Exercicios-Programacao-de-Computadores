"""No planeta Alpha vive a criatura Blobs, que come precisamente  (metade) de seu suprimento de comida disponível todos os dias. Escreva um programa que leia a capacidade inicial de suprimento de comida C, em Kg, e calcule quantos dias passarão antes que Blobs coma todo esse suprimento até restar um quilo ou menos.

Input
A primeira linha de entrada contem um único inteiro N (1 ≤ N ≤ 1000), indicando o número de casos de teste. As N linhas seguintes contém um valor de ponto flutuante C (1 ≤ C ≤ 1000) correspondente à quantidade de comida disponível para Blobs.

Output
Para cada caso de teste, imprima uma linha contendo o número de dias que Blobs irá demorar para comer todo seu suprimento de comida, seguido da palavra "dias"."""



n = int(input())
dias = []
c = []

for i in range(n):
    c.append(float(input()))


for i in range(0, n):
    qtd = 0

    while (c[i] > 1.0):
        c[i] = c[i]/2
        qtd = qtd + 1

    dias.append(qtd)

for i in range(n):
    print(dias[i], "dias")




