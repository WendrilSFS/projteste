def criar_tabela_precos():

    tabela_precos = {}
    preco = 1.99
    for i in range(1, 51):
        preco_total = produto * preco
        tabela_precos[produto] = preco_total
    return tabela_precos

tabela_precos = criar_tabela_precos()

for produto, preco in tabela_precos.items():
    print(f"{produto} itens: R${preco:.2f}")


     
