#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
  
letra = input("Digite uma letra: ").lower()

if letra.isalpha():  # .isalpha() Verifica se é uma letra
    if letra in 'aeiou':
        print("Vogal")
    else:
        print("Consoante")
else:
    print("Entrada inválida! Por favor, digite apenas uma letra.")