pessoas_amigos = {
    "jao" : {'idade': '20 anos', 'cidade': 'CG','profissao' : 'bancario'},
    "jose" : {'idade': '38 anos', 'cidade': 'RJ','profissao' : 'encarregado'},
    "maria" : {'idade': '25 anos', 'cidade': 'PR','profissao' : 'advogada'},
    "marcus" : {'idade': '22 anos', 'cidade': 'CG','profissao' : 'TI'},
}
for nome in pessoas_amigos:
    print(nome)

nome = input("digite um nome: ")
if nome in pessoas_amigos:
    print(f"o nome {nome} esta na lista")
else:
    print(f"o nome {nome} nao esta na lista")