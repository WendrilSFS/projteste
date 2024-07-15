print("ola")

cargo = input("digite o cargo: ")
nome = input("digite seu nome: ")
email = input("digite seu email: ")
idade = int(input("digite sua idade: "))

if(idade >= 18):
    print("Parabens voçe passou para a fase 1")
    curso = input("voce possui curso na area? ")
    if curso == "sim":
        print("parabens voce passou para a fase 2")
        nota = float (input("digite a nota da prova: "))
        if nota >= 7:
            print("Parabens voce passou para a fase final")
        else:
            print("reprovou na etapa final")
    else:
        print("obriagado pela participação")
else:
    print("obrigado pela participação")

