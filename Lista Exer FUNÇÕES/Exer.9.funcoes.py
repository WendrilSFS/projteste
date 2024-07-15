def cilindro(raio,altura):
    volume = 3.14 * raio ** 2 * altura
    print(f"O volume do cilindro é de: {volume}")

raio = float(input("digite o valor do raio: "))
altura = float(input("digite o valor da altura: "))

cilindro(raio,altura)