# potencia de energia
def calcula_valor(consumo,preco):
    valor = consumo * preco
    return valor

# valor = calcula_valor(5,4)
# print(valor)

def calcula_consumo(potencia,horas,preco):
    consumo = potencia * horas / 1000
    conta = calcula_valor(consumo,preco)
    return conta

potencia = int(input("digite a potencia do aparelho: "))
tempo = int(input("quanto tempo foi utilizado no mes: "))
preco = float(input("digite o valor do kwh: "))


banho = calcula_consumo(potencia,tempo,preco)

print("R$: ",banho)
