from Brinquedo import Brinquedo

class Buzz(Brinquedo):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

    def brincar(self):
        return super().brincar()

    def voar(self):
        print(f"{self.nome} esta voando")

item = Buzz("Buzz","verde","20cm",45.70)

item.brincar()
item.voar()