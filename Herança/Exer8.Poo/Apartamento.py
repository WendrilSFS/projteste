from Imovel import Imovel

class Apartamento (Imovel):
    def __init__(self, inscricaomunicipal, valoraluguel, iptu, piscina, sala_de_estar, quartos, aream2, elevador):
        super().__init__(inscricaomunicipal, valoraluguel, iptu)
        self.piscina = piscina
        self.sala_de_estar = sala_de_estar
        self.quartos = quartos
        self.aream2 = aream2
        self.elevador = elevador

    def obter_parcela_iptu(self, parcela):
        return super().obter_parcela_iptu(parcela)
    
    def Valor_Aluguel(self, novovalor):
        return super().Valor_Aluguel(novovalor)
