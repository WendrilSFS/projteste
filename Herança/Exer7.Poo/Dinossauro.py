from Brinquedo import Brinquedo

class Dinossauro (Brinquedo):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

    def brincar(self):
        return super().brincar()
    
    def voz(self):
        print(f"{self.nome} ruge")

item2 = Dinossauro("rex","verde","25cm",23)

item2.brincar()
item2.voz()