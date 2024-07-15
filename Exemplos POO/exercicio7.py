class Agenda:
    def __init__(self, dia, mes, ano, anotacao):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def validarData(self):
        if 1 <= self.dia <= 31 and 1 <= self.mes <= 12 and self.ano > 0:
            return True
        else:
            return False

    def anotarTarefa(self, novaAnotacao):
        self.anotacao = novaAnotacao

    def mostrarAnotacao(self):
        if self.validarData():
            return (f"{self.dia}/{self.mes}/{self.ano}: {self.anotacao}")
        else:
            return ("Data inválida")


dia1=int(input("Digite a o dia: "))
mes1=int(input("Digite o mes: "))
ano1=int(input("Digite o ano: "))
anotacao1=input("Digite a tarefa que deseja salvar no dia: ")

agenda1=Agenda(dia1,mes1,ano1,anotacao1)

agenda1.validarData()
agenda1.mostrarAnotacao()
print(agenda1.mostrarAnotacao())