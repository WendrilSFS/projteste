def notafinal(nota1,nota2,nota3,letra):
    if letra == "A":
        media = nota1 + nota2 + nota3 / 3
        print(f"a media do aluno é de: {media:.2f} pontos")
    elif letra == "P":
        peso = nota1 * 5 + nota2 * 3 + nota3 * 2 / 5 + 3 + 2
        print(F"PESO É IGUAL A: {peso:.2f} ")

n1 = float(input("digite sua primeira nota: "))
n2 = float(input("digite sua segunda nota: "))
n3 = float(input("digite sua terceira nota: "))

notafinal(n1,n2,n3,"A")
notafinal(n1,n2,n3,"P")