class Funcionario:
    def __init__(self,nome,sobrenome,horas_trabalhadas,valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ht = horas_trabalhadas
        self.vh = valor_hora

    def nomecompleto(self):
        self.sobrenome = self.nome + self.sobrenome
        print(self.sobrenome)

    def calcularsalario(self):
        vt = self.ht * self.vh
        print(f"o valor do salario é de R$ {vt}")

    def incrementarHoras(self, novahora):
        self.ht += novahora
        print(self.ht)


colaborador = Funcionario("wendril","souza",10,10)
colaborador.nomecompleto()
colaborador.calcularsalario()
colaborador.incrementarHoras(50)
colaborador.calcularsalario()