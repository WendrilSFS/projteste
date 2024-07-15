class Pessoa:
    def __init__(self, id=0, nome=""):
        self.id=id
        self.nome=nome
    def hello(self):
        print(f"Olá {self.nome}")

pes1=Pessoa()
id=input("Digite sua id: ")
pes1.id=id
nome=input("Digite seu nome: ")
pes1.nome=nome
print(pes1.id)
pes1.hello()
print("Bem vindo a interface de navegação maritima.")