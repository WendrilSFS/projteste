numero = int(input("digite um nume de entre 100 e 9999: "))
while numero < 100 or numero > 9999:
    numero = int(input("numero invalido! digite um numero entre 100 a 9999: "))

unidade = numero % 10
numero //= 10
dezena = numero % 10
numero //= 10
centena = numero % 10
milhar = numero // 10

print(f"unidade {unidade}")
print(f"dezena {dezena}")
print(f"centena {centena}")
print(f"milhar {milhar}")
