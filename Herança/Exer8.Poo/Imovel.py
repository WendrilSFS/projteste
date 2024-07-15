class Imovel:
    def __init__(self,inscricaomunicipal,valoraluguel,iptu):
        self.inscricaomunicipal = inscricaomunicipal
        self.valoraluguel = valoraluguel
        self.iptu = iptu
        print(self.valoraluguel)

    def obter_parcela_iptu(self,parcela):
        self.parcela = parcela
        print(self.parcela)

    def Valor_Aluguel(self,novovalor):
        self.valoraluguel = novovalor
        print(novovalor)

