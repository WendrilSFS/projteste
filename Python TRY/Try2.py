
i = 0
soma = 0
while i < 10:
    try:
        x = int(input("Digite um numero: "))
        soma += x
        i += 1
    except:
        print("NUMERO INVALIDO!! TENTE NOVAMENTE")

print(soma)