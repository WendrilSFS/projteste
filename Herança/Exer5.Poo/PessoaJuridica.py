from PessoaHerdar import Pessoa

class PessoaJuridica (Pessoa):
    def __init__(self, nome, telefone, email, endereco,cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj

    def dados(self):
        print(self.nome)
        print(self.telefone)
        print(self.email)
        print(self.endereco)
        print(self.cnpj)

    def negociar(self):
        print("Pessoa em negociação")

cliente = PessoaJuridica("wendril",99999-9999,"abcd@gmail.com","Mato Grosso","12345678/0001")
cliente.dados()
cliente.negociar()
    