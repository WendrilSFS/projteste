def calculadora (n1,n2,simbolo):
    if simbolo == "+":
        soma = n1 + n2
        print(soma)
    if simbolo == "-":
        subtracao = n1 - n2
        print(subtracao)
    if simbolo == "/":
        divisao = n1 / n2
        print(divisao)
    if simbolo == "*":
        multiplicacao = n1 * n2
        print(multiplicacao)

n1 = float(input("digite um valor: "))
n2 = float(input("digite outro valor: "))

calculadora(n1,n2,"-")
calculadora(n1,n2,"+")
calculadora(n1,n2,"*")
calculadora(n1,n2,"/")