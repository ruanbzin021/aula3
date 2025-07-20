nota1 = float(input("Nota do 1º bimestre: "))
nota2 = float(input("Nota do 2º bimestre: "))

media = (nota1 + nota2) / 2

if media >= 9.0 and media <= 10.0:
  conceito = "A"
  print(f"Nota 1:{nota1}\nNota 2:{nota2}\nMedia:{media}\nConceito:{conceito}\nAprovado!!!")

elif media >= 7.5 and media < 9.0:
  conceito = "B"
  print(f"Nota 1:{nota1}\nNota 2:{nota2}\nMedia:{media}\nConceito:{conceito}\nAprovado!!!")

elif media >= 6.0 and media < 7.5:
  conceito = "C"
  print(f"Nota 1:{nota1}\nNota 2:{nota2}\nMedia:{media}\nConceito:{conceito}\nAprovado!!!")

elif media >= 4.0 and media < 6.0:
  conceito = "D"
  print(f"Nota 1:{nota1}\nNota 2:{nota2}\nMedia:{media}\nConceito:{conceito}\nReprovado!!!")

else:
  conceito = "E"
  print(f"Nota 1:{nota1}\nNota 2:{nota2}\nMedia:{media}\nConceito:{conceito}\nReprovado!!!")
