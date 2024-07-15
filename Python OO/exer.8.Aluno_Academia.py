class Aluno_academia:
    def __init__(self,nome : str,idade : int,peso : float,altura : float,mensalidade=120):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

        
    def obter_valor_mensalidade(self):
        if self.idade < 18:
            return self.mensalidade * 1.5
            
            print(f"o aluno {self.nome} é menor e pagara r$ {self.mensalidade} por mes")
        else:
            print(f"aluno é maior e nao ganhara desconto")
            return self.mensalidade


    def calcularIMC(self):
        indice = self.peso * self.altura * self.altura
        return indice
    
aluno = Aluno_academia("wendril",28,80.6,1,78)

valor = aluno.obter_valor_mensalidade()
print(f"o valor da mensalidade sera de R$ {valor}")

indice = aluno.calcularIMC()
print(f"o desempenho do aluno é de {indice} kg")