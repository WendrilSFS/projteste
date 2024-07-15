class Ingresso:
    def __init__(self,preco,setor):
        self.preco = preco
        self.setor = setor

    def dados(self):
        print(self.preco)
        print(self.setor)


    def altera_preco(self):
        novopreco = float(input("digite o novo valor: "))
        self.preco = novopreco
        print(novopreco)


trabalho = Ingresso(20,"animacao")
trabalho.dados()
trabalho.altera_preco()