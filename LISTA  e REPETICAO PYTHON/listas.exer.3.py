terminou = False
p = i = 0
while (not terminou):
    n = int(input("digite um numero, ou zero para terminar: "))
    if n == 0:
        terminou = True
    else:
        if n % 2 == 0:
            p = p + 1
        else:
            i = i + 1

print("p = ", p)
print("i = ", i)