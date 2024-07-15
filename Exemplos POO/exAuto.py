class Automovel:
    def __init__(self,marca,modelo,ano="2024",placa="ABC-1234"):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.placa=placa
    
    def ligar(self):
        print(f" {self.marca} Ligada!")
    
    def getDados(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Placa: {self.placa}")

carro1=Automovel("BMW","330i",2024,"RWA-4321")
carro1.getDados()
carro1.ligar()