dinheiro = input("Vc tem dinheiro: (sim) ou (nao)? ").strip().lower()
if dinheiro not in ["sim", "nao"]:
    print("Valor inválido! Por favor, digite apenas (sim) ou (nao).")
else:
    tem_dinheiro = dinheiro == "sim"
    senha = input("Digite sua senha: ")
    senha_correta = "88328991"
    senha_ok = senha == senha_correta

    if tem_dinheiro and senha_ok:
        print("Saldo: R$ 77,777.777")
    elif tem_dinheiro and not senha_ok:
        print("Senha Incorreta!!!!!")
    elif not tem_dinheiro and senha_ok:
        print("Saldo Insuficiente!!!!!")
    else:
        print("Sem saldo e senha incorreta!")
