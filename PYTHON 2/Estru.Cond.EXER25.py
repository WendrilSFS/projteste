print("ola")

operacao = input("digite a a operacao [+],[-],[*],[/]: ")

n1 = float(input("digite o numero: "))
n2 = float(input("digite outro numero: "))

if (operacao == "+"):
    res = n1 + n2
    print(f"o resultado da soma é {res}")

elif (operacao == "-"):
    res = n1 - n2
    print(f"o resultado da subtração é {res}")

elif (operacao == "*"):
    res = n1 * n2
    print(f"o resultado da multiplicação é {res}")

elif (operacao == "/"):
    res = n1 / n2
    print(f"o resultado da divisão é {res}")
