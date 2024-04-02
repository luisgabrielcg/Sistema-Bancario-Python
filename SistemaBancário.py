menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        deposito = input("Informe o valor de depósito: ")
        deposito = deposito.replace(",", ".")
        deposito = float(deposito)

        if deposito > 0:
            saldo += deposito
            extrato += f"| R$ {deposito:.2f} adicionado. | \n"
        else:
            print("Erro! Valor informado inválido.")

    elif opcao == "s":

        if numero_saques == LIMITE_SAQUES:
            print("Você já realizou 3 saques hoje. Tente novamente amanhã.")

        else:
            saque = input("Informe o valor de saque: ")
            saque = saque.replace(",", ".")
            saque = float(saque)

            if saque > limite:
                print("Erro! Valor ultrapassa o limite de saque.")

            elif saque > saldo:
                print("Erro! Saldo insuficiente para saque.")

            elif saque <= 0:
                print("Erro! Valor informado inválido.")

            else:
                saldo -= saque
                numero_saques += 1
                extrato += f"| R$ {saque:.2f} sacado. | \n"

    elif opcao == "e":
        print("===============Extrato===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("=====================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")