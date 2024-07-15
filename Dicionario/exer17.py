def armazena_dados_pessoa(**kwargs):
    dados_pessoa = {}

    for chave, valor in kwargs.items():
        dados_pessoa[chave] = valor

    print("Dados da Pessoa:")
    for chave, valor in dados_pessoa.items():
        print(f"{chave}: {valor}")

armazena_dados_pessoa(nome="João", idade=30, cidade="São Paulo")
