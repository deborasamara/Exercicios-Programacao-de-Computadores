valor = int(input())

qtd_cem = valor//100
qtd_cinquenta = (valor%100)//50
qtd_vinte = ((valor%100)%50)//20
qtd_dez = (((valor%100)%50)%20)//10
qtd_cinco = ((((valor%100)%50)%20)%10)//5
qtd_dois = (((((valor%100)%50)%20)%10)%5)//2
qtd_um = ((((((valor%100)%50)%20)%10)%5)%2)//1


print(valor)
print(
    qtd_cem, " nota(s) de R$ 100,00\n",
    qtd_cinquenta, " nota(s) de R$ 50,00\n",
    qtd_vinte, " nota(s) de R$ 20,00\n",
    qtd_dez, " nota(s) de R$ 10,00\n",
    qtd_cinco, " nota(s) de R$ 5,00\n",
    qtd_dois, " nota(s) de R$ 2,00\n",
    qtd_um, " nota(s) de R$ 1,00\n",
    sep = ""
    )