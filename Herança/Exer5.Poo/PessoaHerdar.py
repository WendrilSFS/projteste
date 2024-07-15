class Pessoa:
    def __init__ (self,nome,telefone,email,endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self):
        print("Pessoa em negociacao")

