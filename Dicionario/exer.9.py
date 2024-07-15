def calcularTempo(tempo_minutos):

    valor_hora_minima = 9.00
    
    valor_hora_adicional = 1.50
    
    tempo_minimo_nao_cobrado = 15

    tempo_horas = tempo_minutos / 60
    
    if tempo_minutos <= tempo_minimo_nao_cobrado:
        valor_total = 0
    else:
        valor_total = valor_hora_minima + (tempo_horas - 1) * valor_hora_adicional
    
    pis = valor_total * 0.0033
    cofins = valor_total * 0.0020
    icms = valor_total * 0.17
    
    valor_total_com_impostos = valor_total + pis + cofins + icms
    
    print(f"Recibo do Cliente:")
    print(f"Tempo utilizado: {tempo_minutos} minutos")
    print(f"Valor total: R$ {valor_total:.2f}")
    print(f"Valor com impostos (PIS + COFINS + ICMS): R$ {valor_total_com_impostos:.2f}")

tempo_utilizado = int(input("digite o tempo de estacionamento: "))
calcularTempo(tempo_utilizado)
