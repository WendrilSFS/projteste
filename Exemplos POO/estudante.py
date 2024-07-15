class Estudante: #DEFINIÇÃO DA CLASSE
    def __init__(self,matricula,nome,idade,nota): #METODO DA CONSTRUÇÃO
        self.matricula=matricula # ATRIBUTOS
        self.nome=nome # ATRIBUTOS
        self.idade=idade # ATRIBUTOS
        self.nota=nota # ATRIBUTOS
    
    def hello(self): #METODO
        print(f"Olá {self.nome}")

    def mostrarDados(self): #METODO PARA MOSTRAR TODOS OS DADOS ARMAZENADOS
        print(f"Matricula {self.matricula}")
        print(f"Nome {self.nome}")
        print(f"Idade {self.idade}")
        print(f"Nota {self.nota}")


# aluno=Estudante(1212,"Pedro",18,80)
# print(aluno.nome)
# aluno2=Estudante(1313,"Rafael",19,10)
# print(aluno2.nome)

# aluno2.hello() #CHAMADA DO METODO / AÇÃO
# aluno2.nome="Ana Patricia"# ATRIBUI OUTRO NOME A VARIAVEL ALUNO2
