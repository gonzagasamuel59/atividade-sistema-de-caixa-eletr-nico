nome = input("Digite o nome do cliente: ")
saldo = float(input("Digite o saldo inicial da conta: R$ "))

quantidade_saques = 0
total_sacado = 0

while saldo > 0:
    saque = float(input("\nDigite o valor do saque (0 para encerrar): R$ "))

    if saque == 0:
        break

    elif saque < 0:
        print("Valor inválido. Digite um valor positivo.")

    elif saque > saldo:
        print("Saldo insuficiente. Operação recusada.")

    else:
        saldo -= saque
        quantidade_saques += 1
        total_sacado += saque

        print("Saque realizado com sucesso!")
        print(f"Saldo atual: R$ {saldo:.2f}")

        if saldo == 0:
            print("Saldo esgotado. Atendimento encerrado automaticamente.")
            break

print("RESUMO DO ATENDIMENTO")
print(f"Cliente: {nome}")
print(f"Saques aprovados: {quantidade_saques}")
print(f"Total sacado: R$ {total_sacado:.2f}")
print(f"Saldo final: R$ {saldo:.2f}")