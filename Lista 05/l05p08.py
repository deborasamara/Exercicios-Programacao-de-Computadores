"""Quatro amigos combinaram de jogar tênis em duplas. Cada um dos amigos tem um nível de jogo, que é representado por um número inteiro: quanto maior o número, melhor o nível do jogador.

Os quatro amigos querem formar as duplas para iniciar o jogo. De forma a tornar o jogo mais interessante, eles querem que os níveis dos dois times formados sejam o mais próximo possível. O nível de um time é a soma dos níveis dos jogadores do time.

Embora eles sejam muito bons jogadores de tênis, os quatro amigos não são muito bons em algumas outras coisas, como lógica ou matemática. Você pode ajudá-los e encontrar a menor diferença possível entre os níveis dos times que podem ser formados?

Input
A entrada contém quatro linhas, cada linha contendo um inteiro A, B, C e D (0 ≤ A ≤ B ≤ C ≤ D ≤ 104), indicando o nível de jogo dos quatro amigos.

Output
Seu programa deve produzir uma única linha, contendo um único inteiro, a menor diferença entre os níveis dos dois times formados."""

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
 
jogadores = [n1, n2, n3, n4]
jo = sorted(jogadores)
 
m1 = (jo[0] + jo[3])
m2 = (jo[1] + jo[2])
dif = abs(m1 - m2)
print(int(dif))
