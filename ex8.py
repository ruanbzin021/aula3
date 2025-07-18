int1 = float(input("Informe o valor de um produto R$"))

int2 = float(input("Informe o valor de outro produto R$"))

int3 = float(input("Informe o valor de outro produto R$"))

numero = [int1, int2, int3]
valor_max = max(numero)
valor_min = min(numero)
print(f"O produto mais barato é R${valor_min:,.2f}")
