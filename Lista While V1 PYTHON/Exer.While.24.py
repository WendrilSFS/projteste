def soma_multiplos_3_ou_5():
    total = 0
    numero = 1
    while numero < 1000:
        if numero % 3 == 0 or numero % 5 == 0:
            total += numero
        numero += 1
    return total

resultado = soma_multiplos_3_ou_5()
print(f"A soma dos múltiplos de 3 ou 5 abaixo de 1000 é: {resultado}")
