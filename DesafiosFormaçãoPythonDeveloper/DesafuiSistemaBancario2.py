def menu():
    menu = """
========================== MENU ==========================
[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Usuário
[5] Nova Conta
[6] Listas Contas
[7] Sair
        => """
    return input(menu)

#Solicitado para passar por posição por isso foi usado o "/"
def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        print("\n")
        print("=" * 45 + " DEPÓSITO " + "=" * 45)
        print(f"Depósito com sucesso.\nValor RS: {valor:.2f}")
        texto = f"Depósito: RS:{valor:.2f}\n"
        extrato += texto
        print("=" * 100)
    else:
        print("\nO valor informado é inválido.")
        print("=" * 100)

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$:{valor:.2f}\n"
        print("=" * 45 + " DEPOSITO " + "=" * 45)
        print(f"\nSaque realizado no valor de RS: {valor:.2f}\n")
        print("=" * 100 )
        print("\n====================== Operação realizada com sucesso ======================")
        numero_saques += 1
    else:
        print("\nValor informado é inválido.\n============================================\n Operação falhou!")  
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================== EXTRATO ==================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("============================================")

def criar_usuario_novo(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Usuário com este CPF já cadastrado.")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro - bairro - cidade/sigla estado): ")
    usuarios.append({"Nome: ": nome, "Data_nascimento: ": data_nascimento, "CPF: ": cpf, "Endereço": endereco})
    print("============================ Criado com sucesso ============================")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF: "] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None



def criar_nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("================ CONTA CRIADA ================")
        return {"Agencia: ": agencia, "numero_conta: ": numero_conta, "Usuario: ": usuario}
    else:
        print("Usuário não encontrado com o CPF informado.")
        return None


def listar_contas(contas):
    for conta in contas:
        print(f"\n Agencia: {conta['Agencia: ']}")
        print(f" C/C: {conta['numero_conta: ']}")
        print(f" Titular: {conta['Usuario: ']['Nome: ']}")
        print("=" * 20)

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    numero_conta = 1
    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario_novo(usuarios)

        elif opcao == "5":
            conta = criar_nova_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            print("Saindo do sistema.")
            print("============================================")
            break

        else:
            print("Opção inválida. Por favor, selecione novamente.")
            print("============================================")

main()
