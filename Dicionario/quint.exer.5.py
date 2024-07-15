#usar funcao texto.split()
# dicionario = {}
# frase = input("digite um texto: ")
# palavra = frase.split()
# cont = 0

# for frase in palavra:
#     cont = cont + 1
# dicionario['frase'] = cont
# print(dicionario)


def contar_frequencia_palavras(texto):

    palavras = texto.split()
    
    frequencia = {}
    
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    
    return frequencia

texto_exemplo = input("Digite um texto: ")

frequencia = contar_frequencia_palavras(texto_exemplo)

for palavra, contagem in frequencia.items():
    print(f"{palavra}: {contagem}")
