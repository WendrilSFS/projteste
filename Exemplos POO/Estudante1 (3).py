class Professor:
    def __init__(self,matricula,nome,cpf,idade) -> None:
        self.mat = matricula
        self.name = nome
        self.cpf = cpf
        self.age = idade

    def hello(self):
        print(f"RELLO {self.name}")

    def mostrarDados(self): #MÉTODO
        print(f" Matricula: {self.matricula}")
        print(f" Nome: {self.nome}")
        print(f" CPF: {self.cpf}")
        print(f" Idade: {self.idade}")
