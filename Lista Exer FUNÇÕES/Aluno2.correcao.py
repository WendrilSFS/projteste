class Aluno:
    def __init__(self,nome,ra,notas):
        self.nome = nome
        self.ra = ra
        self.notas = notas

    def mostrarsituacao(self):
        media = sum(self.notas) / len(self.notas)
        if media <5:
            return "reprovdo"
        elif media >=5 and media <= 6.9:
            return "exame"
        else:
            return "aprovado"
        

nome = input("digite o nome: ")
ra = int(input("digite o ra do aluno: "))
notas = []

i = 0 
while i < 4:
    nota = float(input("digite a nota do aluno: "))
    notas.append(nota)
    i = i + 1 

aluno = Aluno(nome,ra,notas)
print(aluno.mostrarsituacao())