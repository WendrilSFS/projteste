import math
n1 = print(input("digite o ponto x1: "))
n2 = print(input("digite o valor y1: "))
n3 = print(input("digite o valor x2: "))
n4 = print(input("digite o valor de y2: "))
res = math.sqrt ((n1-n3)) ** 2 + ((n1 + n4)** 2)

print(f"a distancia entre os ponto é: {res}")

if res > 10:
    print("longe")
else:
    print("perto")
    