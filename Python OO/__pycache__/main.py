from Estudante import Estudante
from Professor import Professor

matricula = input("Matricula: ")
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
nota = input("digite sua nota: ")

aluno1 = Estudante(matricula,nome,idade,nota)

aluno1.mostrardados()