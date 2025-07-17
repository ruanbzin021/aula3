#Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

if n1 > n2:
    print(f"{n1} é maior")
elif n1 < n2:
    print(f"{n2} é maior")

else:
    n1 == n2
    print("Os numeros são iguais")
