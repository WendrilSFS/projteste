# keys mostra o lado esquerdo ou as chaves do dicionario
# values mostra o lado direito ou os valores da chave 

estoque = {
    "cerveja" : "20",
    "salgadinho" : "15",
    "cachaca" : "26",
    "paes" : "30",
    "carvao" : "12",
    "coca cola" : "54",
    "energetico" : "10", 
}
print(estoque.keys())
print(estoque.values())

produto = input("digite o produto: ")
if produto in estoque:
    print(f"o produto {produto} esta com estoque de {estoque[produto]} unidades")
else:
    print("o produto nao esta disponivel")
