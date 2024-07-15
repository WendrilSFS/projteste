numeros = []
i = 0
while len(numeros) < 10:
    numeros.append(int(input("digite um valor: ")))
print(f"A lista dos numeros é: {numeros}")
print(f"O maior numero é: {max(numeros)}")
print(f"O menor numero é: {min(numeros)}")