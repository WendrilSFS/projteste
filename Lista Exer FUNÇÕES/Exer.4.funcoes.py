def horas(hr,mn,seg):
    hr = hr * 3600
    mn = mn * 60
    seg = seg
    res = hr + mn + seg
    print(f"{res} segundos")

a = int(input("digite a hora: "))
b = int(input("digite os minutos: "))
c = int(input("digite os segundos"))

horas(a,b,c)
