# Bootcamp NTT DATA - Engenharia de Dados com Python
# Desafio Sistema Bancário

menu = """
Selecione a operação desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 1000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0: # atendimento a regra onde o sistema não deverá aceitar depositos de valores negativos.
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("Depósito realizado com Sucesso!")
        else:
            print("Houve falha na operação! O valor informado é invalido.")

    elif opcao == "s":
        valor = float(input("Informe o valor desejado para saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Houve falha na operação! Você não possui saldo suficiente. Verifique sua conta!")
        
        elif excedeu_limite:
            print("Houve falha na operação! O valor do saque é maior que o limite disponível. Verifique sua conta!")

        elif excedeu_saques:
            print("Houve falha na operação! Você atingiu o limite diário de saques disponível. Verifique sua conta!")    

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso! Retire o valor solicitado. ")

        else:
            print("Houve falha na operação! O valor informado é invalido. ")

    elif opcao == "e":
        print("\n=================  EXTRATO  =================")
        print("Não há movimentações no período." if not extrato else extrato) # verifica se há movimentações para exibir.
        print(f"\nSaldo: R${saldo:.2f}")
        print("===============================================")

    elif opcao == "q":
        print("Obrigado por ser nosso Cliente!")
        break

    else:
        print("Operação inválida! Selecione novamente a operação desejada. ")    
                            
