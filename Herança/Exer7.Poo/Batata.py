from Brinquedo import Brinquedo

class Batata (Brinquedo):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

    def brincar(self):
        return super().brincar()
    
    def montar(self):
        print(f"{self.nome} monta peças")

item2 = Batata("Senhor Batata","marrom","10cm",60)

item2.brincar()
item2.montar()