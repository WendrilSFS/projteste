class Professor:
    def __init__(self,nome,idade,materia):
        self.nome = nome
        self.idade = idade
        self.materia = materia

    def mostrarDados(self):
       print(f"Nome do Professor: {self.nome}")
       print(f"Idade: {self.idade} anos")
       print(f"Materia: {self.materia}")

prof = Professor("Thiago",30,"DEV")

# prof.mostrarDados()
        