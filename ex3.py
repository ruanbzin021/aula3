#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
print("Qual seu genero?")
sexo = input("Digite (F) para Feminino e (M) para masculino: ")
sexo.lower()

if sexo not in ["f", "m"]:
        print("Sexo inválido! Por favor, digite apenas (f) ou (m).")
