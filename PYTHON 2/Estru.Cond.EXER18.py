print("ola")

salario = float(input("digite o valor do seu salario: "))

prestacao = float(input("digite o valor da prestacao: "))

res = 0.20 * salario

if (prestacao > res):
    print("empretimo consedido")

else:
    print("emprestimo negado")