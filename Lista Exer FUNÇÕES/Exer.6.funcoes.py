def reverso(numero):
    numero = str(numero)
    inverso = "".join(reversed(numero))
    print(inverso)

numero = int(input("digite um numero: "))
reverso(numero)