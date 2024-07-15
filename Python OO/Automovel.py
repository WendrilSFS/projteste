class Automovel:
    def __init__(self,marca,modelo,cor="Branco",ano="2024",placa="ABC-1234"):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.placa = placa

    def ligar(self):
        print(f" {self.marca} Carro Ligado!!!!!")

    def getdados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Ano: {self.ano}")
        print(f"Placa: {self.placa}")

# carro1 = Automovel("BMW","328i")

carro1 = Automovel("BMW","328i","Azul","1999","HRT-2341")
carro1.getdados()
carro1.ligar()