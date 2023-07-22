"""Um determinado material radioativo perde metade de sua massa a cada s segundos. Escreva um programa que leia o tempo s de perda de massa e a massa inicial mi, em gramas, de um material. O programa deve então calcular em quanto tempo a massa do material fica menor do que 0, 5 grama. O programa deve mostrar a massa final, com 3 casas decimais em uma linha e o tempo gasto para o material chegar a essa massa. O tempo deve ser mostrado na forma D dias HH:MM:SS.

Input
A entrada é composta de 1 linha contendo 2 (dois) números inteiros s (1 ≤ s ≤ 109), o tempo, em segundos, que a massa do material cai pela metadee mi, a massa inicial do material radioativo.

Output
Seu programa deve mostrar uma única linha, com o tempo gasto em forma de horas, minutos, segundos e milissegundos: D dias HH:MM:SS."""

s, m_i = map (int, input().split())
x_s = 0

while (m_i >= 0.5):
    x_s = x_s + 1
    m_i = m_i/2

t_segundos = x_s * s

t_dias = t_segundos//86400
t_segundos = t_segundos%86400

t_horas = t_segundos//3600
t_segundos = ((t_segundos%86400)%3600)

t_minutos = (t_segundos//60)

t_segundos = ((t_segundos%60))

print(t_dias, "dias","{:02d}:{:02d}:{:02d}".format(t_horas, t_minutos, t_segundos))







