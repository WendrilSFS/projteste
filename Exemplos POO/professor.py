class Professor: #DEFINIÇÃO DA CLASSE
    def __init__(self,materia,nome,idade,): #METODO DA CONSTRUÇÃO
        self.materia=materia # ATRIBUTOS
        self.nome=nome # ATRIBUTOS
        self.idade=idade # ATRIBUTOS

    def mostrarDados(self):
        print(f"Dados pessoais: {self.nome},{self.idade} anos, Professor de {self.materia}")
    
professor1=Professor("Programação","Thiago Almeida",37)
print(professor1.nome)
professor1.mostrarDados()