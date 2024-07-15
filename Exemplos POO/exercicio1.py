#1 - Classe Pessoa: Crie uma classe que modele uma pessoa. Esta classe deve possuir os seguintes atributos:​
#Nome​, Idade, Endereço 
# A classe deve ter os seguintes métodos:​ Mostrar nome;​Alterar a idade;​Imprimir endereço.​

class Pessoa:
    def __init__(self,nome,idade,endereço):
        self.nome=nome
        self.idade=idade
        self.endereço=endereço

    def getNome(self):
        return self.nome
    
    def setIdade(self, novaIdade):
        self.idade=novaIdade
    def mostraEndereço(self):
        print({self.endereço})

    # def getDados(self):
    #     print(f"{self.nome}")
    #     idade=input("Confirme sua idade: ")
    #     print(f"{self.endereço}")    

pes1=Pessoa("Matheus Sakamoto",18,"Rua tal de tal numero tal")
print(pes1.getNome())
print(pes1.idade)
pes1.setIdade(23)
print(pes1.mostraEndereço())
