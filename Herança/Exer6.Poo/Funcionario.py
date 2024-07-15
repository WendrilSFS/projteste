class Funcionario:
    def __init__(self,nome,matricula,salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario

    def bater_ponto(self,presenca):
        self.presenca = presenca
        print(self.presenca)


