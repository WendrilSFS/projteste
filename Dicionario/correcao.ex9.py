def calculartempo(tempo_em_minuto):
    valor_minuto_por_hora = 9.00
    valor_adicional_por_hora = 1.50

    if tempo_em_minuto < 15:
        return 0.00
    
    horas_completas = tempo_em_minuto // 60
    minutos_restantes = tempo_em_minuto % 60

    if minutos_restantes > 0:
        horas_completas += 1
    
    if horas_completas == 1:
        total = valor_minuto_por_hora
    else:
        total = valor_minuto_por_hora + (horas_completas - 1) * valor_adicional_por_hora
        return total
    
tempo_utilizado = int(input("digite o tempo em minutos: "))
valor_total = calculartempo(tempo_utilizado)
print(f"O valor total a ser pago é: {valor_total:.2f}")

pis = valor_total * 0.0033
cofins = valor_total * 0.0020
icms = valor_total * 0.17

valor_resultado_final = valor_total + pis + cofins + icms

print(f"{valor_resultado_final:.2f}")