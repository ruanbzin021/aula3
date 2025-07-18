try: 
    salario = float(input("Informe seu salario R$"))

    if salario <= 279.99:
        percentual = 20
    # Aumente o salário em 20%
    
    elif salario >= 280 and salario <= 699.99:
        percentual = 15
    # Aumente o salário em 15%
    
    elif salario >= 700 and salario <= 1499.99:
     percentual = 10
    # Aumente o salário em 10%
  
    elif salario >= 1500:
        percentual = 5
    # Aumente o salário em 5%
  
    aumento = salario * (percentual / 100)  
    novo_salario = salario + aumento

    print(f"Salario anterior R${salario:,.2f}")
    print(f"Percentual de aumento aplicado {percentual}%")
    print(f"Aumento de R${aumento:,.2f}")
    print(f"Seu novo salário é R${novo_salario:,.2f}")

except:
    print("Digite seu Salario")
