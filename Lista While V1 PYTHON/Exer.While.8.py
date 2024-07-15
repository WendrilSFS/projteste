lista = []
i = 1
while len(lista) <= 10:
    numero = int(input("digite um numero: "))
    if numero >= 0:
        lista.append(numero)
        i = i + 1
    else:
        numero < 0
        print("inavlido")

    media = sum(lista) / len (lista)
    print(lista)
    print(media)
