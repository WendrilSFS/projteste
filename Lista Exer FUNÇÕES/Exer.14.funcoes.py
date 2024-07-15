def percurso(km,litros):
    carro = km / litros
    if carro < 8:
        print("gasta muito!")
    elif carro < 8 > 15:
        print("economico!")
    else:
        print("super economico!")

km = float(input("digite quantos km: "))
litros = float(input("digite quatos litros: "))
percurso(10,2)