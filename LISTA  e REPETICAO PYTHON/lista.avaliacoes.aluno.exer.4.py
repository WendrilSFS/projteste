numeros = int(input("digite o numero de avaliações: "))
contador = 0

for item in range(numeros):
    notas = int(input("digite o valor das notas: "))
contador = contador + notas
print(contador)


