def calcular_financiamento(valor_veiculo, entrada, taxa_juros, num_parcelas):

    valor_emprestimo = valor_veiculo - entrada

    taxa_juros_mensal = taxa_juros / 12

    parcela_mensal = (valor_emprestimo * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** (-num_parcelas))

    total_pago = parcela_mensal * num_parcelas

    juros_pagos = total_pago - valor_emprestimo

    resultados = {
        "total_pago": total_pago,
        "juros_pagos": juros_pagos,
        "valor_parcela": parcela_mensal
    }

    return resultados

valor_veiculo = float(input("Digite o valor total do veículo: "))
entrada = float(input("Digite o valor da entrada: "))
taxa_juros = float(input("Digite a taxa de juros anual (como decimal): "))
num_parcelas = int(input("Digite o número de parcelas: "))

resultados_financiamento = calcular_financiamento(valor_veiculo, entrada, taxa_juros, num_parcelas)

print("\nDetalhes do Financiamento:")
print(f"Valor total pago: R${resultados_financiamento['total_pago']:.2f}")
print(f"Juros pagos: R${resultados_financiamento['juros_pagos']:.2f}")
print(f"Valor da parcela: R${resultados_financiamento['valor_parcela']:.2f} por mês")
