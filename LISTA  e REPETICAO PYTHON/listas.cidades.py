cidades = []
while len(cidades) < 10:
    nome = input("digite a cidade que voce queria conhecer: ")
    cidades.append(nome)

print(cidades.sort(reverse=True))

