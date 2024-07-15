from Estudante import Estudante
from Professor import Professor


matricula = input("MATRICULA: ")
nome = input("DIGITE SEU NOME: ")
idade = input("DIGITE SUA IDADE: ")
nota = input("NOTA: ")

aluno1 = Estudante(matricula,nome,idade,nota)

aluno1.mostrarDados()
