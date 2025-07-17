#modulo
#print(12 %4 == 0) True

n = float(input("Digite um valor numerico: "))
n = round(n)

if n == 0:
    print("Numero invalido!!!")

elif n %2 == 1:
    print("O numero é impar")

else:
    n %2 == 0
    print("O numero é par")    