class Funcionario:
    def __init__(self,nome,sobrenome,horasTrabalhadas,valorhr):
        self.nome=nome
        self.sobrenome=sobrenome
        self.horasTrabalhadas=horasTrabalhadas
        self.valorhr=valorhr
    
    def nomeCompleto(self):
        print(f"{self.nome} {self.sobrenome}")
    def getSalario(self):
        salario=(self.horasTrabalhadas*self.valorhr)*20
        print(f"O Salário é R${salario}")
    def setValorhr(self,adicaoValorhr):
        self.valorhr+=adicaoValorhr
        print(f"O valor por hr com a adição de R${adicaoValorhr} é R${self.valorhr}")

nomeFuncionario=input("Digite o nome do funcionario: ")
sobrenomeFuncionario=input("Digite o sobrenome: ")
horasTrabalho=int(input("Digite as hrs trabalhadas: "))
valorporhr=float(input("Digite o valor por hr trabalhadas: "))

funcionario1=Funcionario(nomeFuncionario,sobrenomeFuncionario,horasTrabalho,valorporhr)

funcionario1.nomeCompleto()
funcionario1.getSalario()
funcionario1.setValorhr()
funcionario1.getSalario()