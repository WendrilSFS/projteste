class Aluno:
    def __init__(self,nome,ra,nota1,nota2,nota3,nota4):
        self.nome = nome
        self.ra = ra
        self.n1 = nota1
        self.n2 = nota2
        self.n3 = nota3
        self.n4 = nota4

    def nomealuno(self):
        print(self.nome)

    def nra(self):
        print(self.ra)

    def notatotal(self):
        print(f"{self.n1 + self.n2 + self.n3 + self.n4}")

    def mostrarsituacao(self):
        media = (self.n1 + self.n2 + self.n3 + self.n4) / 4
        print(media)
        if media >= 7:
            print("Aprovado")
        elif media < 5:
            print("reprovado")
        else:
            print("exame")


estudante = Aluno("wendril",1010,4,6,5,4)

estudante.notatotal()

estudante.mostrarsituacao()