from Pessoa import Pessoa
class Professor(Pessoa):
    def __init__(self, matricula, nome, idade,formacao,disciplina,cargahora,salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga = cargahora
        self.sal = salario


    def dados(self):
        print(self.formacao)
        print(self.disciplina)
        print(self.carga)
        print(self.sal)

    def lecionar(self):
        print("Professor podera dar a aula")

prof = Professor(1234,"Thiago",32,"Analista de sistema","DEv",44,3500)

prof.dados()
prof.lecionar()