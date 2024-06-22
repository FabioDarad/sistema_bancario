import textwrap
# Criar um sistema bancário simples com depósito, saque e extrato.


def menu():
    menu = """\n

    [d] \t Depositar
    [s] \t Sacar
    [e] \t Extrato
    [nc] \t Nova conta
    [lc] \t Listar contas
    [nu] \t Novo usuário
    [q] \t Sair

    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: \tR$ {valor:.2f}\n'
        print('\n=== Depósito realizado com sucesso. ===')
    else:
        print('\n @@@ Operação falhou. O valor informado é inválido. @@@')
    return saldo, extrato


def sacar(*, saldo, valor, exrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite_diario
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print('Você não tem saldo suficiente.')
    elif excedeu_limite:
        print('Você excedeu seu limite dário.')
    elif excedeu_saques:
        print('Você ultrapassou o limite de saques permitido.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
    else:
        print('Saque falhou. O valor informado é inválido.')
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print('======== EXTRATO ========')
    print('Não foram realizados saques.' if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print('=========================')


def criar_usuario(usuarios):
    cpf = input('Informe o CPF (Somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('\n @@@ Já existe usuário com esse CPF. @@@')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input(
        'Informe o endereço (logradouro, n°, bairro, cidade/estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento,
                    'cpf': cpf, 'endereco': endereco})
    print('=== Usuário criado com sucesso. ===')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0 if usuarios_filtrados else None]


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Digite o número do CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('=== Conta criada com sucesso! ===')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('Usuário não encontrado.')


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C: \t {conta['numero_conta']}
            Titular: \t {conta['usuario']['nome']}
        """
        print('=' * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    #limite_diario = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == 'd':
            valor = float(input('Qual o valor do depósito: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':

            valor = float(input('Qual o valor do saque? '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'q':
            break

        else:
            print('Operação inválida, por favor, selecione uma opção válida.')


main()
