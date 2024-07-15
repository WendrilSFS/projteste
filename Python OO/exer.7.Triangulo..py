class Triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoa = ladoA
        self.ladob = ladoB
        self.ladoc = ladoC

    def perimetro(self):
        perimetro = self.ladoa + self.ladob + self.ladoc
        return perimetro

    def getmaiorlado(self):
        maiorlado = max(self.ladoa,self.ladob,self.ladoc)
        return maiorlado 
    
    def areatriangulo(self):
        base = float(input("digite o valor da base: "))
        altura = float(input("digite o valor da altura: "))
        area = (base * altura) / 2
        return area

a = float(input("digite o valor do primeiro lado: "))
b = float(input("digite o valor do segundo lado: "))
c = float(input("digite o valor do terceiro lado: ")) 

res = Triangulo(a,b,c)

perimetro = res.perimetro()
print(f"o valor do perimetro é: {perimetro}")

lado = res.getmaiorlado()
print(f"o maior lado tem o valor de: {lado}")

area = res.areatriangulo()
print(f"a area do triangulo é de: {area}")
