print("Em que turno você estuda:")
turno = input("(m) para matutino\n(v) para vespertino\n(n) noturno\n").strip().lower()

if turno == "m":
    print("Bom dia")
elif turno == "v":
    print("Boa tarde")
elif turno == "n":
    print("Boa noite")
else:
    print("Digite apenas (m), (v) ou (n)") 
