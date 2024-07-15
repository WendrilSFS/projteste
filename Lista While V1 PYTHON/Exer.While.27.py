def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

A = int(input("Digite um valor para A: "))
fatorial_A = fatorial(A)

print(f"{A}! =", end=" ")
for i in range(A, 0, -1):
    print(i, end="")
    if i > 1:
        print(" X ", end="")
    else:
        print(" =", end="")
print(f" {fatorial_A}")
