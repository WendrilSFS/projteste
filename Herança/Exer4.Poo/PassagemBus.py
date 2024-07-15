class PassagemBus:
    def __init__(self,placa,leito):
        self.placa = placa
        self.leito = leito

    def dados(self):
        print(f"onibus com placa: {self.placa}")
        print(f"numero da proltona: {self.leito}")

    def abastecer(self,tanque):
        self.tanque = tanque
        if self.tanque < 50:
            print("O onibus precisa ser abastecido")
        else:
            print("O onibus pode seguir viajem")

        
        
passageiro = PassagemBus("htb - 4567",25)
passageiro.dados()
passageiro.abastecer(60)