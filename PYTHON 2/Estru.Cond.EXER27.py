print ("ola")

opcao = input ("escolha uma opcao (soma),(subtracao),(multiplicacao),(divisao): ")

n1 = int(input("digite um numero: "))
n2 = int(input("digite outro numero: "))

if (opcao == "soma"):
    res = n1 + n2
    print(f"o resultado da soma é {res}")

elif (opcao == "subtracao"):
    res = n1 - n2
    print(f"a diferença é de {res}")

elif (opcao == "multiplicacao"):
    res = n1 * n2
    print(f"o resultado da multiplicação é {res}")

else:
    (opcao == "divisao")
    res = n1 / n2
    print(f"o resultado da divisão é {res}")