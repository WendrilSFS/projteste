# args (cria valores e salva em tuplas)
# kwargs (cria valores e salva no dicionario)

# def numeros (*args):
#     soma = 0
#     for i in args:
#         soma += i 
#     return soma     

# resultado = numeros(8,9,6,20,46)
# print(resultado)

def soma_argumentos(*args):
    return sum(args)

resultado = soma_argumentos(1, 2, 3, 4, 5)
print(f"A soma dos argumentos é: {resultado}")


