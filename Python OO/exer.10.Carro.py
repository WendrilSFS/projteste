class Carro:
    def __init__(self,modelo,marca,cor,ano,valor,nivel=0,consumo=0):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = nivel
        self.consumo = consumo

    def abastecer(self, litros):
        self.nivel += litros

    def andar(self, distancia_km):
        consumo = distancia_km * self.consumo
        self.nivel -= consumo

    def verificar_nivel(self):
        if self.nivel == 0:
            return 0
        return self.consumo

    def calcular_imposto(self):
        ipva = 0.025 * self.valor
        return ipva


car = Carro(modelo="compacto", marca="chevrolet", cor="Branco", ano=2022, valor=30000, consumo=10)
car.abastecer(50) 
car.andar(100) 
print(f"Nivel gasolina: {car.nivel} litros")
print(f"consumo por km: {car.verificar_nivel()} litros")
print(f"IPVA: {car.calcular_imposto()} ")



