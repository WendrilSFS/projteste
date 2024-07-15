def calcular_potencia(base, expoente):
    resultado = 1
    contador = 0

    while contador < expoente:
        resultado *= base
        contador += 1

    return resultado


base = float(input("Digite o valor da base (x): "))
expoente = int(input("Digite o valor do expoente (y): "))


resultado_potencia = calcular_potencia(base, expoente)


print(f"{base}^{expoente} = {resultado_potencia}")