"""Cássio alugou um carro para a viagem de férias. O carro tem consumo de combustível constante (em kilômetros rodados por litro de combustível), independente da velocidade com que trafega. Ao fim da viagem, Cássio deve devolver o carro no aeroporto. Cássio está terminando sua viagem de férias e está no momento na rodovia que leva ao aeroporto, em direção ao aeroporto para devolver o carro. Mais precisamente Cássio está no último posto de combustível existente na rodovia em que ele pode abastecer o carro antes de devolvê-lo. Para economizar o máximo possível em combustível, Cássio quer devolver o carro com o menor número de litros possível no tanque – idealmente, com o tanque zerado, ou seja, sem combustível. Dados o consumo do carro, a distância em que se encontra do aeroporto e a quantidade de combustível presente no tanque antes do abastecimento, determine qual deve ser a menor quantidade de combustível que Cássio deve comprar

Input
A primeira linha contém um inteiro, C (1 ≤ C ≤ 50), o consumo do carro em kilômetros rodados por litro de combustível. A segunda linha contém um inteiro D (1 ≤ D ≤ 1000), a distância do aeroporto, em kilômetros. A terceira linha contém um inteiro T (1 ≤ T ≤ 100), o número de litros de combustível presente no tanque antes do abastecimento. Você pode assumir que o tanque tem capacidade suficiente para armazenar todo o combustível que Cássio comprar.

Output
Seu programa deve produzir uma única linha, contendo um único valor, com um dígito de precisão, indicando a quantidade de combustível que Cássio deve comprar, para chegar ao aeroporto com o tanque contendo a menor quantidade de combustível possível."""

c_km_l = int(input())
dist_aeroporto_km = int(input())
combust_antes_abast = int(input())

necessario = (dist_aeroporto_km/c_km_l)

quanto_colocar = necessario - combust_antes_abast

if(quanto_colocar < 0):
    print(0.0)
else:
    print("{:.1f}".format(quanto_colocar))