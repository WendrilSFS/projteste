numeros = [2, 3, 4, 7, 8, 11, 5, 9, 12]
cont = 0
print(numeros)

## Parando / encerrando o loop, se 11 for encontrado ##

while cont < len(numeros):
    print("Valor do contador: ",cont, "Item da Lista: ",numeros[cont])
    
    if numeros[cont] == 11:
        print("encontramos o numero 11!")
        break
    else:
        cont = cont + 1 