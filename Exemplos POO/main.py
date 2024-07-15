from estudante import Estudante


matricula=input("Digite a sua matricula: ")
nome=input("Digite seu nome: ")
idade=input("Digite a sua idade: ")
nota=input("Digite a sua nota: ")

aluno1=Estudante(matricula,nome,idade,nota)
aluno1.mostrarDados()
