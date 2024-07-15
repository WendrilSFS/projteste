print("ola")

a = int(input("digite sua idade: "))
b = int(input("digite seu tempo de serviço: "))

if (a >= 65):
    print("já pode aposentar")

elif (b >= 30 ):
    print("ja pode aposentar")

elif (a >= 60) and (b >= 25):
    print("pode aposentar")

else:
    print("ainda não pode aposentar")

