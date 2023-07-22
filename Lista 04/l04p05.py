"""No tabuleiro de xadrez, a casa na linha 1, coluna 1 (canto superior esquerdo) é sempre branca e as cores das casas se alternam entre branca e preta, de acordo com o padrão conhecido como... xadrez! Dessa forma, como o tabuleiro tradicional tem oito linhas e oito colunas, a casa na linha 8, coluna 8 (canto inferior direito) será também branca. Neste problema, entretanto, queremos saber a cor da casa no canto inferior direito de um tabuleiro com dimensões quaisquer: L linhas e C colunas. No exemplo da figura, para L = 6 e C = 9, a casa no canto inferior direito será preta!

nput
A primeira linha da entrada contém um inteiro L (1 ≤ L ≤ 1000) indicando o número de linhas do tabuleiro. A segunda linha da entrada contém um inteiro C (1 ≤ C ≤ 1000) representando o número de colunas.

Output
Imprima uma linha na saída. A linha deve conter um inteiro, representando a cor da casa no canto inferior direito do tabuleiro: 1, se for branca; e 0, se for preta."""

from traceback import print_tb


n_linhas = int(input())
n_colunas = int(input())

x = n_colunas
y = n_linhas

# numeros iguais - branco
if(x == y):
    print(1)

# impar e impar - branco 
elif(x%2 != 0 and y%2 != 0):
    print(1)

# par e par - branco
elif(x%2 == 0 and y%2 == 0):
    print(1)

# impar e par - preto
elif((x%2==0 and y%2 != 0) or (y%2==0 and x%2 !=0)):
    print(0)


# Condições

# Num iguais = branco (1)
# Impar e impar = branco (1)
# par e par = branco (1)
# impar e par = preto (0)
