"""Caio estava brincando de construir triângulos com palitos de diferentes tamanhos. Ele fazia isso juntando as pontas de três palitos sobre uma mesa. Ele notou que podia agrupar os triângulos formados em três grupos:

Triângulos acutângulos, que são aqueles em que todos os ângulos internos medem menos de 90°; Triângulos retângulos, que são aqueles que possuem um ângulo interno que mede exatamente 90°; Triângulos obtusângulos, que são aqueles que possuem um ângulo interno que mede mais de 90°. Ele também percebeu que nem sempre é possível formar um triângulo com três palitos.

Sua tarefa é, dados os comprimentos A, B e C de três palitos, dizer se é possível formar um triângulo com esses palitos e, em caso afirmativo, dizer a qual grupo o triângulo formado pertence.

Input
A entrada consiste de uma única linha, contendo três inteiros A, B e C (1 ≤ A, B, C ≤ 104) separados por espaço.

Output
Imprima uma linha contendo apenas uma letra minúscula:

'n' se não for possível formar um triângulo;
'a' se o triângulo formado for acutângulo;
'r' se o triângulo formado for retângulo;
'o' se o triângulo formado for obtusângulo."""

n1, n2, n3 = map(int, input().split())

# Se é possível formar um triângulo
if ( (n1 < n2 + n3) and (n2 < n1 + n3) and (n3 < n1 + n2) ):

    #Retângulo
    if ( ( n1**2 == n2**2 + n3**2 ) or ( n2**2 == n1**2 + n3**2 ) or ( n3**2 == n1**2 + n2**2 ) ):
        print("r")

    #Acutângulo 
    elif( (n1**2 < n2**2 + n3**2) and (n2**2 < n1**2 + n3**2) and (n3**2 < n1**2 + n2**2) ):
        print("a")
    
    #Obstusângulo
    elif( (n1**2 > n2**2 + n3**2) or (n2**2 > n1**2 + n3**2) or (n3**2 > n1**2 + n2**2) ):
       print("o")

# Se não é possível formar
else:
    print("n")

