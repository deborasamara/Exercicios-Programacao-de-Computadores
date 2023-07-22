nome_vendedor = str(input())
salario_fixo = float(input())
t_vendas = float(input())

salario_total = salario_fixo + (0.15*t_vendas)

print(nome_vendedor)
print("R$", "{:.2f}".format(salario_total))