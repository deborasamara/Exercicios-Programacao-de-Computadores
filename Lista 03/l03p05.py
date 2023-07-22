"""Para se preparar para os outros problemas, vamos fazer um teste. Dado um número X, retorne o menor número par maior do que X.

Input
Uma linha contendo um número x (0 < x < 107).

Output
Uma linha contendo a resposta do problema."""

num = int(input())

if(num%2==0):
    num_retorno = num + 2

else:
    num_retorno = num + 1

print(num_retorno)