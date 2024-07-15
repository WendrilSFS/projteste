class Estudante: ## Definição da classe
    def __init__(self,matricula,nome,idade,nota):
        self.matricula = matricula
        self.nome = nome ## Atributo
        self.idade = idade
        self.nota = nota

    def hello(self): ## método
        print(f"Olá {self.nome}")

    def mostrardados(self): ## método
        print(f"Matricula {self.matricula}")    
        print(f"Nome {self.nome}")
        print(f"Idade {self.idade}")
        print(f"Nota {self.nota}") 


aluno = Estudante(1212,"João",18,80)

# print("O aluno chama-se:", aluno.nome)

# aluno.hello()
# aluno.nome = "Wendril"

# aluno.mostrardados()