numeros = []
i = 1
while len(numeros) < 10:
    numeros.append(int(input("digite um valor: ")))
print(f"A lista dos numeros é: {numeros}")
print(f"A soma dos numeros é: {sum(numeros)}")
