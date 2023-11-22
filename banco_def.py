def menu():
    menu = """\n
    ================ MENU ================
    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q] \tSair
    Opção: """
    return str(input(menu)).lower().strip()


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\nDepósito efetuado!")
    else:
        print("\nValor não é válido. Tente novamente.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(f"\nFalha! Saldo insuficiente. Seu saldo é R$ {saldo}")
    elif excedeu_limite:
        print(f"\nFalha! Saque máximo por dia é de R$ {limite}.")
    elif excedeu_saques:
        print(f"\nFalha! Somente {limite_saques} saques por dia.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque efetuado!")
    else:
        print("\nValor não é válido. Tente novamente.")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Nenhuma movimentação no dia." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = int(input("Número CPF(somente número): "))
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nUsuário já cadastrado!")
        return
    nome = input("Nome: ")
    data_nascimento = input("Data nascimento(dd-mm-aaaa): ")
    endereco = input("Endereço(rua, nº - bairro - cidade/estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nConta criada!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não cadastrado, criação de conta negada!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def main():
    limite_saques = 3
    agencia = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Valor: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Valor: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato,
            limite=limite, numero_saques=numero_saques, limite_saques=limite_saques,)
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Opção inválida. Tente novamente")


main()
