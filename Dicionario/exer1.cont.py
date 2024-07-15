def tabela(preco, produto):
    tabela = preco * produto
    return tabela
print("Loja Quase Dois - Tabela de")
preco = 1.99 
produto = 0

while produto < 50:
    produto = produto + 1
    result = tabela(produto,preco)
    print(f"O {produto} o valor é: {result}")

