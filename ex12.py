try:
    valor_hora = float(input("Quanto você ganha por hora? R$ "))
    horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

    salario_bruto = valor_hora * horas_trabalhadas

    if salario_bruto <= 900:
        ir = 0
        ir_percent = "Isento"
    elif salario_bruto <= 1500:
        ir = salario_bruto * 0.05
        ir_percent = "5%"
    elif salario_bruto <= 2500:
        ir = salario_bruto * 0.10
        ir_percent = "10%"
    else:
        ir = salario_bruto * 0.20
        ir_percent = "20%"

    sindicato = salario_bruto * 0.03
    fgts = salario_bruto * 0.11

    total_descontos = ir + sindicato
    salario_liquido = salario_bruto - total_descontos

    print("\nResumo do cálculo:")
    print(f"Salário Bruto:R$ {salario_bruto:.2f}")
    print(f"IR ({ir_percent}):R$ {ir:.2f}")
    print(f"Sindicato (3%):R$ {sindicato:.2f}")
    print(f"FGTS (11%):R$ {fgts:.2f}")
    print(f"Total de Descontos:R$ {total_descontos:.2f}")
    print(f"Salário Líquido:R$ {salario_liquido:.2f}")

except:
    print("Digite valores válidos!")
