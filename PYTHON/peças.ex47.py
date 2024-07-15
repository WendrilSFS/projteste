print("ola")

n1 = float(input("digite hora de trabalho"))
n2 = float(input(" digite a quantidade de horas extras"))

x = n1 * 32.50
y = n2 * 44.50

result = x + y
print("valor bruto", result)

inss = result * 0.11
print("valor liquido",result - inss)

           