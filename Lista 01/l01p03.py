from decimal import Decimal
from tokenize import Double


raio = float(input())

area = 3.14159 * (raio**2)

print("A=","{:.4f}".format(area), sep="")
