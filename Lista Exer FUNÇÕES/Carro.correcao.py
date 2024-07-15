class Carro:
    def __init__(self,modelo,marca,cor,ano,valor,nivel=5):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = nivel

    def calcularimposto(self):
        imposto = (self.valor * 2.5) / 100
        return imposto

    def abastecer(self,quat_litros):
        self.nivel = self.nivel + quat_litros

    def andar(self,km):
        consumo = km / 10.8
        self.nivel -= consumo
        print(f"o carro gastou {consumo:.2f} litros")

    def verificarnivel(self):
        return self.nivel



car1 = Carro("Jetta","Volks","Prata",2022,120000)

print(car1.calcularimposto())

print("nivel de gasolina",car1.nivel,"litros")
car1.abastecer(45)
print("Nivel de gasolina",car1.nivel,"litros")

car1.andar(50)

tanque = car1.verificarnivel()
print(f"a quantidade restante é de {tanque:.2f} litros")
