print("suave gurizada")

a = float(input("digite sua primeira nota: "))
b = float(input("digite sua segunda nota: "))

if (a >= 0 and a <= 10) and (b >= 0 and b <= 10):
    print(f"sua nota {a}, e nota {b} estao validas")

else:
    print("notas invalidas")

media = (a + b) / 2

print(f"a media de suas notas é {media}")