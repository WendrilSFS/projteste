print("ola")

n1= float(input("digite a nota do trabalho do laboratorio: "))
n2 = float(input("digite a nota da avaliacao semestral: "))
n3 = float(input("digite a nota do exame final: "))

media = (n1 + n2 + n3) / 3 

print(f"A media do aluno é {media}")

if media < 3:
    print("o aluno esta reprovado")

elif media >= 3 and media < 6 :
    print("o aluno esta de recuperção")

else:
    print("o aluno esta aprovado")
    
