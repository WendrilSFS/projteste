def calcular_salario(horas_trabalhadas):
    salario_base_por_semana = 40 * salario_hora_base
    salario_excedente_por_semana = 0
    
    if horas_trabalhadas > 40:
        horas_excedentes = horas_trabalhadas - 40
        salario_excedente_por_semana = horas_excedentes * (salario_hora_base * 1.5)
        salario_total = salario_base_por_semana + salario_excedente_por_semana
    else:
        salario_total = horas_trabalhadas * salario_hora_base
    
    return salario_total


salario_hora_base = float(input("Informe o salário por hora base: "))


horas_trabalhadas = float(input("Informe o número de horas trabalhadas na semana: "))


salario_total = calcular_salario(horas_trabalhadas)
print("O salário total a ser pago é: R$", salario_total)