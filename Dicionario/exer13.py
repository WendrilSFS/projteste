def lista_padrao(quantidade_elementos,valor_padrao):
    valor = quantidade_elementos * valor_padrao
    return valor

quantidade = int(input("digite a quantidade de elementos: "))
valor = input("digite o valor: ")

x = lista_padrao(quantidade,valor)

lista = []
lista.append(x)
print(lista)



