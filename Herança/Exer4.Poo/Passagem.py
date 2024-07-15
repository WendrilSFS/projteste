class Passagem:
    def __init__(self,preco,assento):
        self.preco = preco
        self.assento = assento

    def dados(self):
        print(self.preco)
        print(self.assento)

    def alterarpreco(self,novopreco):
        self.preco = novopreco
        print(novopreco)
    
    def escolherassento(self,cadeira):
        self.assento = cadeira
        print(cadeira)


passageiro = Passagem(150,75)
passageiro.dados()

novopreco = float(input("digite o novo preco: "))

cadeira = int(input("digite o numero do assento; "))

passageiro.alterarpreco(novopreco)

passageiro.escolherassento(cadeira)