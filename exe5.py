nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"\nMédia alcançada: {media:.2f}")

if media == 10.0:
    print("Aluno aprovado com distinção!")
elif media >= 7.0:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")