print("ola")

a = float(input("diigite o valor: "))
b = float(input("digite o valor: "))
c = float(input("digite o valor: "))

if (a == b) or (b == c):
    print("o triangulo é equilatero")

elif (a == b) and (b == c) and (c != a):
    print("o triangulo é isosceles")

else:
    (a != b) and (b != c) and (c != a)
    print("o triangulo é escaleno")
