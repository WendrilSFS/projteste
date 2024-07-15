###### crie uma lista com 5 numeros inteiros #####
##### imprima o tamanho da lista #####
##### adicione 5 numeros decimais usando append #####
#### remova os dois ultimos intens da lista #####
#### imprima o tamanho da lista #####
##### imprima a lista ordenada #####
#### imprima o maior e menor numero da lista #####
#### imprima a lista em ordem crescente #####
#### imprima a soma e media ######
#### acrescente mais dois itens na posicao 0 e 1 #####


print("ola")

numeros = [5,10,15,20,25]
print(numeros)
print(len(numeros))

numeros.append(2.5)
numeros.append(5.5)
numeros.append(4.3)
numeros.append(9.9)
numeros.append(15.5)
print(numeros)

numeros.pop()
numeros.pop()
print(numeros)

print(len(numeros))

print(sorted(numeros))

print("Maior numero: ",max(numeros))
print("Menor numero: ",min(numeros))
print(numeros)

print(numeros.sort(reverse=True))
print(numeros)

print("Soma: ",sum(numeros))

print("Media: ",sum(numeros) / len(numeros))

numeros.insert(0,4)
numeros.insert(1,6)

print(numeros)

