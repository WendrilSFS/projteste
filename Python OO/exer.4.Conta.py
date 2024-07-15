class Conta:
    def __init__(self,nome,cpf,numero,saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    
    def dadosusuario(self):
        print(f"NOme: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Numero: {self.numero}")
        print(f"Saldo da Conta: R$ {self.saldo}")

    def depositar(self):
        setdeposito = float(input("digite a quantidade de deposito: "))
        self.saldo += setdeposito
        print(self.saldo)
        print(f"saldo final: {self.saldo}")


    def sacar(self):
        saque = float(input("digite a quantidade do saque: "))
        if self.saldo > 0 and saque <= self.saldo:
            self.saldo -= saque
            print("saldo disponivel pode sacar!!")
            print(f"saldo final: {self.saldo}")  
        else:
            print("Saldo insuficiente")


print("Ola, seja bem vindo")
nome = input("digite seu nome: ")
cpf = int(input("digite seu cpf: "))
numero = int(input("didgite seu numero: "))
saldo = float(input("digite o saldo de sua conta: "))

usuario = Conta(nome,cpf,numero,saldo)
usuario.dadosusuario()
usuario.depositar()
usuario.sacar()

    


    