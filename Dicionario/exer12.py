# def calcular_media(lista):
#     soma = 0
#     for num in lista:
#         soma += num
#     media = soma / len(lista)
#     return media

# listanumerica = [2,3,4,5,7,9,11,15]

# x = calcular_media(listanumerica)

# print(x)

def calcular_media(lista):
    media = sum(lista) / len(lista)
    return media

listanumerica = [2,3,4,5,7,9,11,15]

x = calcular_media(listanumerica)

print(x)