## Tratamento de Exceção 

x = 500
y = 0

#Tente realizar o calculo
try:
    res = x / y
    print(res)
except:
    print("Erro ao tentar realizar calculo")
finally:
    y = int(input("digite o Y novamente: "))
    res = x / y
    print(f"Resultado: {res}")
