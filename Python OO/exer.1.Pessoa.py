# def getnome(self):
    #     return self.nome
## mostrar funçao


# def setidade(self,novaidade):
    # self.idade = novaidade
## alterar  funcao
    

class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    
    def setidade(self,novaidade):
        self.idade = novaidade


    def mostardados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"endereço: {self.endereco}")

pessoa = Pessoa("Wendril",18,"Afonso Pena")
pessoa.mostardados()

pessoa.setidade(23)
pessoa.mostardados()


