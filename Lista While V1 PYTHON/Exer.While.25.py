soma = 0
contador = 0


idade = int(input("Digite a idade (ou 0 para sair): "))


while idade != 0:
    soma = soma + idade
    contador += 1
    idade = int(input("Digite a idade (ou 0 para sair): "))


if contador > 0:
    media = soma / contador
    print(f"A média das idades é {media:.2f}")
else:
    print("Nenhuma idade foi informada.")