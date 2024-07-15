contador = 0
pares = 0
while True:
     numero = int(input("Digite um número inteiro (0 para sair): "))
     if numero == 0:
            break

     contador = contador + 1
     if numero % 2 == 0:
            pares = pares + 1

print(f"Total de números lidos: {contador}")
print(f"Total de valores pares: {pares}")
