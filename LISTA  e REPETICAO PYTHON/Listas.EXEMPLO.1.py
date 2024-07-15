print("ola")

numeros = [15,6.67,28,11,5,99,67.5,55,]
print(numeros)

##### tamanho da lista####
print(len(numeros))

##### posicao da lista ####
print(numeros[5])

##### soma de variavel da lista #####
print(numeros[3] + numeros[7])

##### soma total da lista #####
print("Soma: ",sum(numeros))

##### maior numero #####
print("Maior numero: ",max(numeros))

### menor numero #####
print("Menor numero: ",min(numeros))

##### organizar lista em ordem do maior para o menor #####
lista_ordenada = sorted(numeros)
print(lista_ordenada)

#### lista em ordem decrescente####
print(numeros.sort(reverse=True))
print(numeros)

##### media da lista ####
print("Media: ", sum (numeros) / len (numeros))

#### index identificar indice atraves do parametro ####
print(numeros.index(99))

#### remover o ultimo item da lista ####
numeros.pop()
print(numeros)
print(len(numeros))

#### inserir item a lista ####
numeros.insert(0,"85")
numeros.insert(2,2000)
print(numeros)

#### adicionar um item na ultima posiçao da lista ####
numeros.append(1000)
numeros.append("wendril")
numeros.append([10,15,20,25])
print(numeros[10])
print(numeros)