from PessoaHerdar import Pessoa

class PessoaFisica (Pessoa):
    def __init__(self, nome, telefone, email, endereco,cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf

    def dados(self):
        print(self.nome)
        print(self.telefone)
        print(self.email)
        print(self.endereco)
        print(self.cpf)

    def negociar(self):
        return super().negociar()
    
cliente = PessoaFisica("wendril","99999-9999","wendril@gmail.com","mato grosso","123456789-09")

cliente.dados()

cliente.negociar()