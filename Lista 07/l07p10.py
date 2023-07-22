"""Na calçada em frente ao Palácio Imperial, não se sabe a razão, existe uma sequência de N números desenhados no chão. A sequência tem a seguinte forma: ela começa e termina com o número 1; apenas os números 1 e 2 aparecem nela; e o número 2 aparece pelo menos uma vez. Veja um exemplo na coluna (a) da figura ao lado. Ninguém sabe o significado da sequência e, justamente por isso, várias teorias malucas surgiram. Uma delas diz que a sequência representa, na verdade, apenas um valor que estaria relacionado a um segredo dos imperadores. Esse valor é a quantidade máxima de números da sequência que poderiam ser marcados com um círculo, de modo que a sequência de números marcados não contenha dois números iguais consecutivos. A coluna (b) da figura ao lado ilustra uma sequência de 4 números marcados que obedece a restrição acima. Só que é possível marcar 7 números, como mostra a coluna (c) da figura.

Neste problema, dada a sequência original de números desenhados no chão da calçada, seu programa deve computar e imprimir a quantidade máxima de números da sequência que poderiam ser marcados com um círculo sem que haja dois números iguais consecutivos na sequência marcada.

Input
A primeira linha da entrada contém um inteiro N (3 ≤ N ≤ 500) representando o tamanho da sequência. As N linhas seguintes contêm, cada uma, um inteiro Vi (1 ≤ Vi ≤ 2), para 1 ≤ i ≤ N, definindo a sequência de números desenhados no chão da calçada imperial.

Output
Seu programa deve imprimir uma linha contendo um número inteiro representando a quantidade máxima de números da sequência que poderiam ser marcados com um círculo sem que haja dois números iguais consecutivos na sequência marcada."""

t_sequencia = int(input())
sequencia = []
v_m = 0

for i in range(t_sequencia):
    sequencia.append(int(input()))

for i in range(0, t_sequencia-1):
    if (sequencia[i] != sequencia[i+1]):
        v_m = v_m + 1

print(v_m+1)
