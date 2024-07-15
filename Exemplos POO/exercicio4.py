class Conta:
    def __init__(self,nome,cpf,numero,saldo=5500):
        self.nome=nome
        self.cpf=cpf
        self.numero=numero
        self.saldo=saldo
    
    def depositar(self,deposito):
        self.saldo=deposito + self.saldo
            
    def sacar(self,saque):
        if self.saldo <0:
            print("Saldo insuficiente")
        else:
            self.saldo=self.saldo-saque
            print("O saldo atual é de ", self.saldo)
    
    def imprimirSaldo(self,saldo):
        self.saldo=saldo
        print(f"Seu saldo é {self.saldo}")

nomeCliente=input("Digite o seu nome: ")
cpfcliente=int(input("Digite seu CPF: "))
numero=int(input("Digite seu número: "))

conta1=Conta(nomeCliente,cpfcliente,numero,)

depositarConta=float(input("Digite o valor a ser depositado: "))
conta1.depositar(depositarConta)
print(conta1.saldo)
sacarConta=float(input("Digite o valor a ser sacado: "))
conta1.sacar(sacarConta)