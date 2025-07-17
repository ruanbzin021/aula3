valor = input("Digite um número: ")

try:
    numero = int(valor)
    print(f"Você digitou o número {numero}")
except ValueError:
    print("Valor inválido! Por favor, digite apenas números.")