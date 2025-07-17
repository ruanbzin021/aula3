#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n1 = int(input("Digite um numero: "))

if n1 > 0:
    print(f"{n1} é positivo")
elif n1 < 0:
    print(f"{n1} é negativo")

else:
    n1 == 0
    print("Os numeros são iguais")
