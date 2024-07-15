class Brinquedo:
    def __init__(self,nome,cor,tamanho,preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        print(f"estou brincando com o brinquedo {self.nome}")
