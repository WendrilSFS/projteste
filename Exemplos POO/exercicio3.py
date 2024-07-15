class Aluno:
    def __init__(self,nome,ra,nota1,nota2,nota3,nota4):
        self.nome=nome
        self.ra=ra
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3
        self.nota4=nota4

    def mostrarSituacao(self):
        media=(self.nota1+self.nota2+self.nota3+self.nota4)/4
        if media >=7:
            print(f"O Aluno {self.nome} >>> Aprovado.")
        elif media >5 and media <6.9:
            print(f"O Aluno {self.nome} >>>Exame.")
        else:
            print(f"O Aluno {self.nome} >>>Reprovado.")

nomeAluno=input(f"Digite o nome do aluno: ")
raAluno=int(input("Digite o RA do aluno: "))
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: ")) 
nota3=float(input("Digite a terceira nota: "))
nota4=float(input("Digite a quarta nota: "))

aluno1=Aluno(nomeAluno,raAluno,nota1,nota2,nota3,nota4)
aluno1.mostrarSituacao()