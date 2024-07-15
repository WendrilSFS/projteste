print ("ola")

preco = 50
aqs = 0.45
aqs2 = 0.30

produto = float(input("digite o valor do produto: "))

if preco < 50:
    produto = preco * aqs
else:
    produto = aqs2 * aqs2
    print(f"o valor é de {produto}")

