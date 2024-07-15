from Funcionario import Funcionario
class Vendedor (Funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome, matricula, salario)
 
    def bater_meta(self):
        print(f"{self.nome} bateu a meta!")

