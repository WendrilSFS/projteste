n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

s = 0
m = 1

for i in range(int(n1), int(n2) + 1):
    if i % 2 == 0:
        s = s + i
else:
    m = m * i

print(f"Soma dos números pares: {s}")
print(f"Multiplicação dos números ímpares: {m}")