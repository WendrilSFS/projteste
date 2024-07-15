class Circulo:
    def __init__(self,raio):
        self.raio = raio

    def valorraio(self):
        print(self.raio)

    def valorarea(self):
        area = 3.14 * self.raio ** 2
        return area      
    
    def valorcircunferencia(self):
        circunferencia = 2 * 3.14 * self.raio
        return circunferencia
        
    
# r = float(input("digite o valor do raio: "))

conta = Circulo(5)

conta.valorraio()

area = conta.valorarea()
print(area)
circunferencia = conta.valorcircunferencia()
print(circunferencia)
