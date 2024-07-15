def data(dia,mes,ano):
    meses = ["nada", "janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
    print(f"{dia} de {meses[mes]} de {ano}")

data(1,2,2020)

dia = int(input("digite a data de hoje: "))
mes = int(input("digite o mes: "))
ano = int(input("digite o ano: "))

data(dia,mes,ano)
