print("ola")

n1 = float(input("digite a nota da primeira prova: "))
n2 = float(input("digite a nota da segunda prova: "))
n3 = float(input("digite a nota da terceira prova: "))

media = (((n1 * 1) + (n2 * 1) + (n3 * 2)) / 4) *10

print(f"sua media é de {media}")

if media >= 70:
    print("Aprovado")

elif media <70 and media >= 30:
    print("recuperação")
else:
    print("reprovado")
