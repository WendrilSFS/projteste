terminar = False
notas = []
while terminar == False:
    nota = int(input("Digite um numero: "))
    if nota >= 0 and nota <= 10:
        notas.append(nota)
    else:
        terminar = True
print(f"A média é: {sum(notas) / len(notas)}")