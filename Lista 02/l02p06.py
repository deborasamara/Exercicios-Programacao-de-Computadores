#Escreva um programa que leia a distância entre duas cidades A e B, em kilômetros, a velocidade, em km/h, do carro e mostre qual o tempo da viagem entre A e B, no formato HH:MM. Os segundos devem ser desprezados.

#Input
#A entrada é composta de 2 linhas. A primeira linha contém um inteiro representando a distância D (1 ≤ D ≤ 1000) entras as cidades. A segunda também contém um número inteiro V (1 ≤ V ≤ 250), que representa a velocidade em km/h.

#Output
#Seu programa deve mostrar uma única linha com o tempo de deslocamento no formato HH:MM. Os segundos devem ser desprezados.

dist_KM = int(input())
velocidade_kmh = int(input())

horas = int(dist_KM/velocidade_kmh)
minutos = int(((dist_KM/velocidade_kmh)*60)%60)

print("{:02d}".format(horas),"{:02d}".format(minutos), sep=":")


