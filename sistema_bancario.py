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


saldo = 0
limite_diario = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
       
    opcao = menu()

    if opcao == 'd':
        valor = float(input('Qual o valor do depósito: '))

        saldo, extrato = depositar(saldo, valor, extrato)
    
    elif opcao == 's':

        valor = float(input('Qual o valor do saque? '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_diario
        excedeu_saques = numero_saques > LIMITE_SAQUES

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
        

    elif opcao == 'e':
        print('======== EXTRATO ========')
        print('Não foram realizados saques.' if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print('=========================')
    
    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor, selecione uma opção válida.')

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: \tR$ {valor:.2f}\n'
        print('\n=== Depósito realizado com sucesso. ===')
    else:
        print('\n @@@ Operação falhou. O valor informado é inválido. @@@')
    return saldo, extrato

def sacar(*, saldo, valor, exrato, limite, numero_saques, limite_saques):


def exibir_extrato(saldo, /, *, extrato):


def criar_usuario(usuarios):


def filtrar_usuario(cpf, usuarios):
