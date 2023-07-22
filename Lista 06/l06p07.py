"""Escreva uma função que receba uma data no formato dia/mes/ano, verifique se é uma data válida, e retorne a data por extenso.

Input
A função recebe 3 (três) valores inteiros dia (1 ≤ dia ≤ 31 ), mes (1 ≤ mes ≤ 12) e ano ( - 10000 ≤ ano ≤ 10000), que representam a data, onde d é o dia, m é o mês e a é o ano.

Output
A função deve retornar uma string contendo a data escrita por extenso.

Assinatura da função em Python:

def dia(dia, mes, ano)

O dia deve ser formatado com exatamente dois algarismos. Caso a data não seja válida a função deve retornar Data Invalida.

Os nomes dos meses devem ser escritos em minúsculas, sem acentos, sem cedilha.

Considere o mês de fevereiro sempre com 28 dias. Não é necessário verificar se é um ano bissexto."""

def dia(dia, mes, ano):
    meses = {
        1: 'janeiro',
        2: 'fevereiro',
        3: 'marco',
        4: 'abril',
        5: 'maio',
        6: 'junho',
        7: 'julho',
        8: 'agosto',
        9: 'setembro',
        10: 'outubro',
        11: 'novembro',
        12: 'dezembro'
    }
    if (mes <=12 and mes>=1):
        #Meses com 31 dias
        if(mes == 1 or mes == 3 or mes ==5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
            if(dia <= 31):
                return  f'{dia:02d} de {meses[mes]} de {ano}'
            else:
                return "Data Invalida"
        
        #Meses com 30 dias
        elif(mes == 4 or mes == 6 or mes == 9 or mes == 11 ):  
            if(dia <= 30):
                return f'{dia:02d} de {meses[mes]} de {ano}'
            else:
                return "Data Invalida"
        
        #Mes com 28 dias
        elif (mes == 2):
            if(dia <= 28):
                return f'{dia:02d} de {meses[mes]} de {ano}'
            else:
                return "Data Invalida"
    else:
        return "Data Invalida"