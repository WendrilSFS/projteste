class Circulo:
    def __init__(self,raio):
        self.raio=raio
    def getRaio(self):
        print(f"O Raio tem o valor de {self.raio}")
    def getArea(self):
        areaCirculo=3.14*(self.raio**2)
        print(f"A área do circulo do raio {self.raio} é {areaCirculo}")
    
    def getCircunferencia(self):
        circunferencia=(3.14**2)*self.raio
        print(f"A circunferência do circulo de raio de {self.raio} é {circunferencia}")

raio=float(input("Digite o valor do raio: "))
circulo1=Circulo(raio)
circulo1.getRaio()
circulo1.getArea()
circulo1.getCircunferencia()