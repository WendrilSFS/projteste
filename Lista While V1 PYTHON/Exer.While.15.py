n1 = int(input("digite um numero: "))

if n1 %2 == 0:
    while n1 >= 0:
        print(n1)
        n1 = n1 - 2

else:
    print("Numero não é par")