# crie um programa, utilizando dicionarios, que solicite ao usuario inserir
# quatro notas e mostre na tela as notas e a media

notas = {
    "nota 1" : float(input("digite a primeira nota: ")),
    "nota 2" : float(input("digite a segunda nota: ")),
    "nota 3" : float(input("digite a terceira nota: ")),
    "nota 4" : float(input("digite a quarta nota: ")),
}
print(notas)

n1 = notas["nota 1"]
n2 = notas["nota 2"]
n3 = notas["nota 3"]
n4 = notas["nota 4"]

media = ((n1 + n2 + n3 + n4) / 4)
print(f"a media é igual a {media}")