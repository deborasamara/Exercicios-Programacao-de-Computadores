"""Cibele, Camila e Celeste são três irmãs inseparáveis. Estão sempre juntas e adoram fazer esportes, ler, cozinhar, jogar no computador... Agora estão aprendendo a programar computadores para desenvolverem seus próprios jogos.

Mas nada disso interessa para esta tarefa: estamos interessados apenas nas suas idades. Sabemos que Cibele nasceu antes de Camila e Celeste nasceu depois de Camila.

Dados três números inteiros indicando as idades das irmãs, escreva um programa para determinar a idade de Camila.

Input
A entrada é composta por três linhas, cada linha contendo um número inteiro N (5 ≤ N ≤ 100), a idade de uma das irmãs.

Output
Seu programa deve produzir uma única linha, contendo um único número inteiro, a idade de Camila."""

i1 = int(input())
i2 = int(input())
i3 = int(input())

if ((i1<=i2 and i1>=i3) or (i1>=i2 and i1<=i3)):
    print(i1)

elif((i2<=i3 and i2>=i1) or (i2>=i3 and i2 <i1)):
    print(i2)

elif((i3>=i1 and i3<=i2) or (i3<=i1 and i3>=i2)):
    print(i3)
