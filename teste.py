menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[f] Fechar
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques=0

while True:
    opcao=input(menu)
    if opcao=="d":
        valor=float(input("Qual o valor do Deposito: "))
        if valor>0: # Evitar que seja valor negativo
            saldo+=valor 
            extrato+=f"Depósito: R$ {valor:.2f}\n" #faz uma concatenação com o extrato 
        else:
            print("Falha, o valor informado é negativo.")
    elif opcao=="s":
        valor=float(input("Informe o valor do saque: "))
        excedeu_saldo=valor > saldo # esse e abaixo verifica se n excedeu nehuma regra de negocio do sacar
        excedeu_limite=valor > 500
        excedeu_saques=numero_saques >= 3
        if excedeu_saldo:
            print("Falha, saldo Insuficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor>0:
            saldo-=valor
            extrato+=f"Saque: R$ {valor:.2f}\n"
            numero_saques+=1
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "e": #printa o extrato, bonito feito assim
        if extrato="" :
            print("Nenhuma operação feita")
        else:
            print(extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
    elif opcao == "f":
        break

    else:
        print("Não existe essa operação,por favor selecione novamente a operação desejada.")
