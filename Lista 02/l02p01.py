nome_funcionario = str(input())
h_trabalhadas = int(input())
valor_ht = float(input())

salario =  h_trabalhadas*valor_ht

print(nome_funcionario)
print("R$", "{:.2f}".format(salario))