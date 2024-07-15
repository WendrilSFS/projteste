class PassagemAviao:
    def __init__(self,portaodeembarque,checkin):
        self.embarque = portaodeembarque
        self.checkin = checkin

    def dados(self):
        print(f" Embarque no portão: {self.embarque}")
        print(f"Numero de checkin: {self.checkin}")

    def decolar(self):
        print("Passageiros embarcados")
        print("Pista liberada...Aviao está pronto para decolar")


embarcar = PassagemAviao(7,12345)
embarcar.dados()
embarcar.decolar()