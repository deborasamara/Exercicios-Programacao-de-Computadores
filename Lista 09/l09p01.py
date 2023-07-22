"""Um jogo de estratégia, com J jogadores, é jogado em volta de uma mesa. O primeiro a jogar é o jogador 1, o segundo a jogar é o jogador 2 e assim por diante. Uma vez completada uma rodada, novamente o jogador 1 faz sua jogada e a ordem dos jogadores se repete novamente. A cada jogada, um jogador garante uma certa quantidade de Pontos de Vitória. A pontuação de cada jogador consiste na soma dos Pontos de Vitória de cada uma das suas jogadas.

Dado o número de jogadores, o número de rodadas e uma lista representando os Pontos de Vitória na ordem em que foram obtidos, você deve determinar qual é o jogador vencedor. Caso mais de um jogador obtenha a pontuação máxima, o jogador com pontuação máxima que tiver jogado por último é o vencedor.

Input
A entrada consiste de duas linhas. A primeira linha contém dois inteiros J e R, o número de jogadores e de rodadas respectivamente (1 ≤ J, R ≤ 500). A segunda linha contém J × R inteiros, correspondentes aos Pontos de Vitória em cada uma das jogadas feitas, na ordem em que aconteceram. Os Pontos de Vitória obtidos em cada jogada serão sempre inteiros entre 0 e 100, inclusive.

Output
Seu programa deve produzir uma única linha, contendo o inteiro correspondente ao jogador vencedor."""

n_jogadores, n_rodadas = map(int, input().split())
pontos_a_distribuir = list(map(int, input().split()))

# 9
m = n_jogadores * n_rodadas

# 9 - 3 = 6
s = m - n_jogadores

# 8
valor = m - 1

# valores da ultima rodada
u_rodada = []


while valor >= s:

    #as últimas posições são os primeiros números
    u_rodada.append(int(pontos_a_distribuir[valor]))
    print(pontos_a_distribuir[valor], "posição:", valor)

    valor = valor - 1


valor = -1
vencedor = 0

for i in range(len(u_rodada)):
    if u_rodada[i] > valor:
        u_rodada.sort
        valor = u_rodada[i]
        vencedor = u_rodada.index(valor)


print("valor: ",valor, "ultima rodada: ",u_rodada, "vencedor", vencedor)













