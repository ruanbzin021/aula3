#modulo
#print(12 %4 == 0) True

n = input("Digite um valor numerico: ")

try:
    numero = int(n)

    if numero == 0:
        print("Numero invalido!!!")
    elif numero % 2 == 1:
        print("O numero é impar")
    else:
        print("O numero é par")
                    
except:
    print("Valor inválido! Por favor, digite apenas números.")