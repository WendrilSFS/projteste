
def media_numeros (*args):
    return sum(args)  / len(args)

resultado = media_numeros(1,2,3,4,5)
print(resultado)



def media (*args):
    if not args:
        return 0.0
    soma = sum (args)
    quantidade = len(args)
    media = soma /quantidade
    return media

resultado1 = media(1.5, 2.5, 3.5)
resultado2 = media(10.0, 20.0, 30.0)
resultado3 = media(7.5, 14.5, 21.5, 28.5)

print(f"Media dos argumentos: {resultado1:.2f}")
print(f"Media dos argumentos: {resultado2:.2f}")
print(f"Media dos argumentos: {resultado3:.2f}")


# def calcular_media(*args):
#     # Verifica se há argumentos
#     if len(args) == 0:
#         return None
    
#     # Calcula a soma dos argumentos
#     soma = sum(args)
    
#     # Calcula a média
#     media = soma / len(args)
    
#     return media

# # Exemplo de uso da função
# argumentos = [2.5, 3.7, 1.8, 4.2]
# resultado = calcular_media(*argumentos)
# print(f"A média dos argumentos {argumentos} é {resultado:.2f}")
