
1
def produto_de_tres(a, b, c):
    produto = a * b * c
    print(f"O produto de {a}, {b}, e {c} é: {produto}")

# Exemplo de uso:
produto_de_tres(2, 3, 4)


2
def exponenciacao(base, expoente):
    resultado = base ** expoente
    return resultado

# Exemplo de uso:
resultado = exponenciacao(2, 3)
print(f"{2} elevado a {3} é: {resultado}")

3
def quantidade_de_digitos(numero):
    # Converte o número para string e calcula o comprimento da string
    # Usa abs() para lidar com números negativos
    num_str = str(abs(numero))
    quantidade = len(num_str)
    print(f"O número {numero} tem {quantidade} dígitos.")

# Exemplo de uso:
quantidade_de_digitos(12345)
quantidade_de_digitos(-9876)
quantidade_de_digitos(0)


4
def verificar_positivo_ou_negativo(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

# Exemplo de uso:
resultado1 = verificar_positivo_ou_negativo(10)
resultado2 = verificar_positivo_ou_negativo(-5)
resultado3 = verificar_positivo_ou_negativo(0)

print(f"O resultado para 10 é: {resultado1}")
print(f"O resultado para -5 é: {resultado2}")
print(f"O resultado para 0 é: {resultado3}")


5
def somaImposto(taxaImposto, custo):
    # Converte a taxa de imposto de porcentagem para decimal
    taxa_decimal = taxaImposto / 100
    # Calcula o custo com o imposto
    novo_custo = custo + (custo * taxa_decimal)
    return novo_custo

# Exemplo de uso:
taxa = 10  # 10% de imposto
custo_inicial = 100  # Custo inicial do item
custo_final = somaImposto(taxa, custo_inicial)

print(f"O custo inicial era: R$ {custo_inicial:.2f}")
print(f"Com uma taxa de imposto de {taxa}%, o custo final é: R$ {custo_final:.2f}")

6
def montar_tabela_precos():
    preco_por_item = 1.99
    print("Lojas Quase Dois - Tabela de Preços")
    for quantidade in range(1, 51):
        total = quantidade * preco_por_item
        print(f"{quantidade} - R$ {total:.2f}")

# Exemplo de uso:
montar_tabela_precos()

7
def calcular_salario(horas_trabalhadas, salario_por_hora):
    # Definindo a carga horária base e a taxa de horas extras
    carga_horaria_base = 40
    taxa_horas_extras = 1.5
    
    if horas_trabalhadas <= carga_horaria_base:
        # Se o funcionário trabalhou 40 horas ou menos
        salario = horas_trabalhadas * salario_por_hora
    else:
        # Se o funcionário trabalhou mais de 40 horas
        horas_extras = horas_trabalhadas - carga_horaria_base
        salario_base = carga_horaria_base * salario_por_hora
        salario_horas_extras = horas_extras * salario_por_hora * taxa_horas_extras
        salario = salario_base + salario_horas_extras
    
    return salario

# Exemplo de uso:
horas_trabalhadas = 45
salario_por_hora = 20  # Suponha que o salário por hora é R$ 20,00
salario_total = calcular_salario(horas_trabalhadas, salario_por_hora)

print(f"O salário total para {horas_trabalhadas} horas trabalhadas é: R$ {salario_total:.2f}")

8
def calcular_excesso_e_multa(peso_peixes):
    # Limite estabelecido pelo regulamento de pesca do MS
    limite_peso = 50
    # Valor da multa por quilo excedente
    valor_multa_por_quilo = 4.00

    # Calcula o excesso de peso
    excesso = max(0, peso_peixes - limite_peso)
    # Calcula a multa
    multa = excesso * valor_multa_por_quilo

    # Imprime os resultados
    print(f"Peso total de peixes: {peso_peixes} kg")
    if excesso > 0:
        print(f"Excesso de peso: {excesso} kg")
        print(f"Valor da multa: R$ {multa:.2f}")
    else:
        print("Não há excesso de peso.")
        print("Valor da multa: R$ 0.00")

# Exemplo de uso:
peso_peixes = float(input("Digite o peso total de peixes (em kg): "))
calcular_excesso_e_multa(peso_peixes)

9
def calcularTempo(tempo_em_minutos):
    # Define os valores das tarifas
    valor_minimo_por_hora = 9.00
    valor_adicional_por_hora = 1.50
    
    # Se o tempo for menor que 15 minutos, não cobra nada
    if tempo_em_minutos < 15:
        return 0.00
    
    # Calcula o número de horas, arredondando para cima
    horas_completas = tempo_em_minutos // 60
    minutos_restantes = tempo_em_minutos % 60
    
    # Se há minutos restantes, conta como uma hora adicional
    if minutos_restantes > 0:
        horas_completas += 1
    
    # Calcula o custo total
    if horas_completas == 1:
        total = valor_minimo_por_hora
    else:
        total = valor_minimo_por_hora + (horas_completas - 1) * valor_adicional_por_hora
    
    return total

# Exemplo de uso:
tempo_utilizado = int(input("Digite o tempo utilizado em minutos: "))
valor_total = calcularTempo(tempo_utilizado)
print(f"O valor total a ser pago é: R$ {valor_total:.2f}")

10
def calcularTempo(tempo_em_minutos):
    # Definindo as tarifas
    valor_minimo_por_hora = 9.00
    valor_adicional_por_hora = 1.50
    
    # Definindo as taxas de impostos
    taxa_PIS = 0.0033
    taxa_COFINS = 0.0020
    taxa_ICMS = 0.17
    
    # Se o tempo for menor que 15 minutos, não cobra nada
    if tempo_em_minutos < 15:
        return 0.00, 0.00, 0.00, 0.00, 0.00
    
    # Calculando o número de horas, arredondando para cima
    horas_completas = tempo_em_minutos // 60
    minutos_restantes = tempo_em_minutos % 60
    
    if minutos_restantes > 0:
        horas_completas += 1
    
    # Calculando o custo total
    if horas_completas == 1:
        total = valor_minimo_por_hora
    else:
        total = valor_minimo_por_hora + (horas_completas - 1) * valor_adicional_por_hora
    
    # Calculando os impostos
    PIS = total * taxa_PIS
    COFINS = total * taxa_COFINS
    ICMS = total * taxa_ICMS
    imposto_total = PIS + COFINS + ICMS
    total_com_impostos = total + imposto_total
    
    return total, PIS, COFINS, ICMS, imposto_total, total_com_impostos, horas_completas

# Exemplo de uso:
tempo_utilizado = int(input("Digite o tempo utilizado em minutos: "))
total, PIS, COFINS, ICMS, imposto_total, total_com_impostos, horas_completas = calcularTempo(tempo_utilizado)

print(f"TEMPO: {horas_completas:.1f} HORAS")
print(f"PIS: R$ {PIS:.2f}")
print(f"COFINS: R$ {COFINS:.2f}")
print(f"ICMS: R$ {ICMS:.2f}")
print(f"IMPOSTO: R$ {imposto_total:.2f}")
print(f"TOTAL: R$ {total_com_impostos:.2f}")

11
def calcular_financiamento(valor_veiculo, entrada, taxa_juros, num_parcelas):
    # Calculando o valor financiado após a entrada
    valor_financiado = valor_veiculo - entrada
    
    # Convertendo a taxa de juros de porcentagem para decimal
    taxa_juros_decimal = taxa_juros / 100
    
    # Calculando o valor total a ser pago utilizando a fórmula de juros compostos
    valor_total_pago = valor_financiado * (1 + taxa_juros_decimal) ** num_parcelas
    
    # Calculando o valor dos juros pagos
    juros_pagos = valor_total_pago - valor_financiado
    
    # Calculando o valor de cada parcela
    valor_parcela = valor_total_pago / num_parcelas
    
    # Exibindo as informações
    print(f"Valor do veículo: R$ {valor_veiculo:.2f}")
    print(f"Valor da entrada: R$ {entrada:.2f}")
    print(f"Valor financiado: R$ {valor_financiado:.2f}")
    print(f"Taxa de juros: {taxa_juros:.2f}% ao mês")
    print(f"Quantidade de parcelas: {num_parcelas}")
    print(f"Valor total pago: R$ {valor_total_pago:.2f}")
    print(f"Valor dos juros pagos: R$ {juros_pagos:.2f}")
    print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")

# Solicitando os dados ao usuário
valor_veiculo = float(input("Digite o valor do veículo: R$ "))
entrada = float(input("Digite o valor da entrada: R$ "))
taxa_juros = float(input("Digite a taxa de juros mensal (%): "))
num_parcelas = int(input("Digite a quantidade de parcelas: "))

# Calculando o financiamento
calcular_financiamento(valor_veiculo, entrada, taxa_juros, num_parcelas)

#Desafio

# 3. Faça um programa, utilizando Dicionários, que peça para o usuário inserir quatro notas e mostre na tela as notas e a média entre elas.

def calcular_media(notas):
    soma = sum(notas.values())
    media = soma / len(notas)
    return media

# Solicita ao usuário inserir as quatro notas
notas = {}
for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas[f"Nota {i+1}"] = nota

# Calcula a média das notas
media = calcular_media(notas)

# Exibe as notas e a média
print("\nNotas inseridas:")
for chave, valor in notas.items():
    print(f"{chave}: {valor}")
print(f"Média: {media:.2f}")


# 4-4. Faça um programa, utilizando Dicionários, que:

# 1° Passo: Peça para o usuário inserir quatro coisas em uma “Caixa Misteriosa” .

# 2° Passo: Peça para o usuário inserir um número.

# 3° Passo: Mostre na tela o que foi inserido na posição do número inserido pelo usuário.

# Passo 1: Solicitar ao usuário inserir quatro coisas na "Caixa Misteriosa"
caixa_misteriosa = {}
for i in range(4):
    coisa = input(f"Insira a {i+1}ª coisa na Caixa Misteriosa: ")
    caixa_misteriosa[i+1] = coisa

# Passo 2: Solicitar ao usuário inserir um número
numero = int(input("Insira um número de 1 a 4 para descobrir o que há na Caixa Misteriosa: "))

# Passo 3: Mostrar na tela o que foi inserido na posição do número inserido pelo usuário
if numero in caixa_misteriosa:
    print(f"Na posição {numero} da Caixa Misteriosa, temos: {caixa_misteriosa[numero]}")
else:
    print("Número inválido. Por favor, insira um número de 1 a 4.")