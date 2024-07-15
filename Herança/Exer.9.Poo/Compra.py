class Compra:
    def __init__(self,numero,produto,valor,valor_total=0):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valortotal = valor_total

    def calcular_valor_total(self):
        icms = 0.17 * self.valor
        frete = 0.05 * self.valor
        self_valor_total = self.valor + icms + frete
        print(self_valor_total)