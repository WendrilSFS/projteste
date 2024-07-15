from Brinquedo import Brinquedo

class Carrinho (Brinquedo):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

    def brincar(self):
        return super().brincar()
    
    def andar(self):
        print(f"{self.nome} esta andando")

item2 = Carrinho("carro","vermelho","15cm",59.70)

item2.brincar()
item2.andar()