"""Em diversas competições acadêmicas, como a Olimpíada Brasileira de Informática (OBI), uma certa quantidade de competidores se classifica de uma fase para a fase seguinte, garantindo uma das vagas disponíveis. Entretanto, normalmente essa quantidade é variável, pois dada uma certa quantidade mínima de classificados, é frequente que haja empate na última vaga de classificação. Neste caso, é comum que todos os competidores empatados na última colocação se classifiquem.
Sua tarefa é ajudar a calcular o número de competidores classificados para a próxima fase. Você receberá uma lista de pontuações obtidas pelos competidores e o número mínimo de vagas para a fase seguinte e você deve decidir quantos competidores de fato vão se classificar.

Input
A primeira linha da entrada contém um número inteiro N, 1 ≤ N ≤ 1000, representando o número de competidores. A segunda linha conterá um inteiro K, 1 ≤ K ≤ N, indicando o número mínimo de competidores que devem se classificar para a próxima fase. Em seguida, N linhas conterão, cada uma um número entre 1 e 1000, inclusive, correspondente á pontuação de um competidor.

Output
Seu programa deve imprimir uma linha, contendo o número de classificados para a próxima fase."""

import collections

n_competidores = int(input())
min_proxima_fase = int(input())
pontuacoes = []
repetidos = []


for i in range(n_competidores):
    pontuacoes.append(int(input()))

pontuacoes.sort(reverse=True)

repetidos = collections.Counter(pontuacoes)

x = list(repetidos.values())

qtd = 0
i = 0
while qtd<min_proxima_fase:
    qtd = qtd + x[i]
    i = i+1

print(qtd)

