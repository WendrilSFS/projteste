from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, notas = list):
        super().__init__(matricula, nome, idade)
        self.notas = notas

    def calcular_media(self):
        media = sum(self.notas)/len(self.notas)
        print(media)

    def estudar(self):
        print("o aluno esta estudando")

aluno = Aluno(123,"Wendril",23,[6,7,8,9])
aluno.calcular_media()
aluno.estudar()


