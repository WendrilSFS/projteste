## Exercicio 1 

# def valores(a, b, c):
#     resultado = a * b * c
#     return resultado

# x = valores(12,12,12)
# print(x)

### Exercicio 2

# def exponencial(a, b):
#     res = a ** b
#     return res

#  x = exponencial(4,4)
#  print(x)

# x = exponencial(int(input("digite o valor da base: ")), int(input("digite o valor do expoente: ")))
# print(x)

## Exercicio 3

# def quantidade_digitos(x):
#     return len(str(x))

# print(quantidade_digitos(1000))
# print(quantidade_digitos(int(input("digite um numero: "))))

## Exercicio 4

# def valor(num):
#     if num > 0:
#         return "Positivo"
#     else:
#         return "Negativo"

# x = valor(-5)
#  x = valor(int(input("digite um numero: ")))
# print(x)

## Exercicio 5

# def soma_imposto(taxa, custo):
#     taxa = taxa / 100
#     imposto = taxa * custo
#     return custo + imposto

# resultado = soma_imposto (float(input("digite o valor da taxa: ")), float(input("digite o valor do custo: ")))
# print(resultado)  

### correção exer 5

def somaimposto(taxaimposto,custo):
    taxa_decimal = taxaimposto / 100
    novo_custo = (custo * taxa_decimal)
    return novo_custo

taxa = 10
custo_inicial = 325
custo_final = somaimposto(taxa,custo_inicial)

print(f"o custo inicial era: R$ {custo_inicial}")
print(f"Com uma taxa de imposto de {taxa}%, o custo final : {custo_final:.2f}")
