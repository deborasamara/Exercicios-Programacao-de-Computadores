"""O principal prêmio da Olimpíada Brasileira de Informática é o convite para os cursos de programação oferecidos no Instituto de Computação da Unicamp, com todas as despesas pagas pela Fundação Carlos Chagas, patrocinadora da OBI. São convidados apenas os competidores que atingem um certo número mínimo de pontos, consideradas as duas fases de provas. Você foi contratado pela Coordenação da OBI para fazer um programa que, dados os números de pontos obtidos por cada competidor em cada uma das fases, e o número mínimo de pontos para ser convidado, determine quantos competidores serão convidados para o curso na Unicamp. Você deve considerar que
todos os competidores participaram das duas fases;
o total de pontos de um competidor é a soma dos pontos obtidos nas duas fases;
Por exemplo, se a pontuação mínima para ser convidado é 435 pontos, um competidor que tenha obtido 200 pontos na primeira fase e 235 pontos na segunda fase será convidado para o curso na Unicamp. Já um competidor que tenha obtido 200 pontos na primeira fase e 234 pontos na segunda fase não será convidado.

Input
A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado). A primeira linha da entrada contém dois números inteiros N e P, representando respectivamente o número de competidores (1 ≤ N ≤ 1000) e o número mínimo de pontos para ser convidado (1 ≤ P ≤ 1000). Cada uma das N linhas seguintes contém dois números inteiros X e Y indicando a pontuação de um competidor em cada uma das fases (0 ≤ X ≤ 400) e (0 ≤ Y ≤ 400).

Output
Seu programa deve imprimir na saída padrão uma única linha contendo um único inteiro, indicando o número de competidores que serão convidados a participar do curso na Unicamp."""

n_competidores, n_min_ser_convidado = map(int, input().split())
pontuacoes1 = []
pontuacoes2 = []
passa = 0

for i in range(n_competidores):
    x, y = map(int, input().split())

    pontuacoes1.append(x)
    pontuacoes2.append(y)

for i in range(n_competidores):
    if( pontuacoes1[i] + pontuacoes2[i] >= n_min_ser_convidado):
        passa += 1
    
print(passa)
