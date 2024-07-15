def imprime(lista):
    cont = 0
    while cont < len(lista):
        print(f"{cont+1}, {lista[cont]}")
        cont += 1
    

listadecompra = ['mamao','castanha','mel','uva','banana','detergente']

imprime(listadecompra)
