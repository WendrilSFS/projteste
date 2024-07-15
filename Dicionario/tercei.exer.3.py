traducao = {
    "hello" : "hola",
    "good morning" : "buen dia",
    "good afternoon" : "buenas tardes",
    "good nigth" : "buenas noches",
    "great week" : "gran friki",
    "good job" : "buen trabajo",
    "godbye" : "adios",
    "hot" : "caliente",
}

traduzir = input("digite a palavra do dicionario para traduzir: ")

if traduzir in traducao:
    print(traducao[traduzir])
else:
    print("nao pode ser traduzida")