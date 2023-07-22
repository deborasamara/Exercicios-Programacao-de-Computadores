"""A turma do colégio vai fazer uma excursão na serra e todos os alunos e monitores vão tomar um teleférico para subir até o pico de uma montanha. A cabine do teleférico pode levar C pessoas no máximo, contando alunos e monitores, durante uma viagem até o pico. Por questão de segurança, tem que ter pelo menos um monitor dentro da cabine junto com os alunos. Por exemplo, se cabem C = 10 pessoas na cabine e a turma tem A = 20 alunos, o colégio poderia fazer três viagens: a primeira com 8 alunos e um monitor; a segunda com 6 alunos e um monitor; e a terceira com 6 alunos e um monitor. Você consegue ver que não seria possível fazer apenas duas viagens?

Dados como entrada a capacidade C da cabine e o número total A de alunos, você deve escrever um programa para calcular o número mínimo de viagens do teleférico.

Input
A primeira linha da entrada contém um inteiro C (2 ≤ C ≤ 100), representando a capacidade da cabine. A segunda linha da entrada contém um inteiro A (1 ≤ A ≤ 1000), representando o número total de alunos na turma.

Output
Seu programa deve imprimir uma linha contendo um número inteiro representando o número mínimo de viagens do teleférico para levar todos os alunos até o pico da montanha."""

c = int(input())
t_alunos = int(input())

total_viagens = t_alunos/(c-1)

if(t_alunos % (c-1)>0):
    total_viagens = total_viagens + 1

print(int(total_viagens))