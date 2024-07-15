from Funcionario import Funcionario

class Gerente (Funcionario):
    def __init__(self, nome, matricula, salario, senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha

    def alterar_senha(self, novasenha):
        self.senha = novasenha

colaborador = Gerente("wendril",1234,4000,2345)

colaborador.alterar_senha(1234)
