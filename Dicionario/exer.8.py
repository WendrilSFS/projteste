def calcular_multa(peso_peixes):
    limite_peso = 50
    excesso = max(0, peso_peixes - limite_peso)
    multa = excesso * 4
    return excesso, multa


peso_peixes = float(input("Digite o peso dos peixes (em Kg): "))

excesso, multa = calcular_multa(peso_peixes)

print(f"Excesso de peso: {excesso:.2f} Kg")
print(f"Multa a ser paga: R$ {multa:.2f}")