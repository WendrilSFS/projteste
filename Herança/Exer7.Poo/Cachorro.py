from Brinquedo import Brinquedo

class Cachorro (Brinquedo):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

    def brincar(self):
        return super().brincar()
    
    def late(self):
        print(f"{self.nome} late")

item2 = Cachorro("totó","marrom","45cm",45)

item2.brincar()
item2.late()