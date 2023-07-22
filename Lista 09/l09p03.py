"""Você está de volta em seu hotel na Tailândia depois de um dia de mergulhos. O seu quarto tem duas lâmpadas. Vamos chamá-las de A e B. No hotel há dois interruptores, que chamaremos de I1 e I2. Ao apertar I1, a lâmpada A troca de estado, ou seja, acende se estiver apagada e apaga se estiver acesa. Se apertar I2, ambas as lâmpadas A e B trocam de estado.

As lâmpadas inicialmente estão ambas apagadas. Seu amigo resolveu bolar um desafio para você. Ele irá apertar os interruptores em uma certa sequência, e gostaria que você respondesse o estado final das lâmpadas A e B.

Input
A primeira linha contém um número N (1 ≤ N ≤ 105) que representa quantas vezes seu amigo irá apertar algum interruptor. Na linha seguinte seguirão N números, que pode ser 1, se o interruptor I1 foi apertado, ou 2, se o interruptor I2 foi apertado.

Output
Seu programa deve imprimir dois valores, em linhas separadas.

Na primeira linha, imprima 1 se a lâmpada A estiver acesa no final das operações e 0 caso contrário. Na segunda linha, imprima 1 se a lâmpada B estiver acesa no final das operações e 0 caso contrário."""

qtd_apertou = int(input())
i_apertados = list(map(int, input().split()))
estado_A = [0]
estado_B = [0]

for i in range(qtd_apertou):

    #interruptor i1 (Modifica lâmpada A )

    #Lâmpada A
    if(i_apertados[i] == 1):

        if(estado_A[0] == 0):
            estado_A[0] = int(1)
        else:
            estado_A[0] = int(0)
            
    #interruptor i2 (Modifica lâmpada A e B)
    elif(i_apertados[i] == 2):

        #Lâmpada A
        if(estado_A[0] == 0):
            estado_A[0] = int(1)
        else:
            estado_A[0] = int(0)

        #Lâmpada B
        if(estado_B[0] == 0):
            estado_B[0] = int(1)
        else:
            estado_B[0] = int(0)

    
print(*estado_A ,"\n", *estado_B, sep="")



        
    

