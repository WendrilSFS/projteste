from Brinquedo import Brinquedo

class Wood (Brinquedo):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

    def brincar(self):
        return super().brincar()
    
    def lacar(self):
        print(f"{self.nome} laça")

item2 = Wood("wood","marrom","30cm",25.70)

item2.brincar()
item2.lacar()