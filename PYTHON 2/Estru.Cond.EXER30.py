print("ola")

a = float(input("digite o valor do produto: "))
b = input("digite seu estado se for [ms], [sp], [rj], [mg]: ")

if (b == "ms"):
    res = a * 0.08
    print(f"o valor em {b} é {res}")

elif (b == "sp"):
    res1 = a * 0.12
    print(f"o valor em {b} é {res1}")

elif (b == "mg"):
    res2 = a * 0.07
    print(f"o valor em {b} é {res2}")

elif (b == "rj"):
    res3 = a * 0.15
    print(f"o valor em {b} é {res3}")

else:
    print("estado invalido")



