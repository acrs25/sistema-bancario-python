from datetime import datetime
import re


def verificar_cpf(clientes, /, *, cpf):

    cpf = re.sub(r"\D", "", cpf)

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return True
    return False


def verificar_duplicidade_conta(cadastro_conta, contas, /):

    for dado in contas:

        if dado["conta"] == cadastro_conta["conta"]:
            return True
    return False


def verificar_limite_transacoes(LIMITE_TRANSACOES, extrato, /):

    data_hoje = datetime.now().strftime("%d/%m/%Y")
    total_transacao_diaria = 0

    for operacao_dia in extrato:
        if data_hoje in operacao_dia:
            total_transacao_diaria += 1

    if total_transacao_diaria >= LIMITE_TRANSACOES:
        print("\n\033[31mLimite de transações diárias atingido!\033[0m\n")
        print("=== Operação permitida: Extrato ===\n")
        return True

    return False


def verificar_restricao_deposito(*, valor):

    if valor <= 0:
        print("\n\033[31mO valor do depósito não pode ser negativo!\033[0m\n")
        return True
    return False


def verificar_saques_dia(*, qtde_saques, SAQUES_DIARIOS):

    if qtde_saques >= SAQUES_DIARIOS:
        print("\n\033[31mSaque diário Excedido\033[0m\n")
        return True
    return False


def verificar_restricao_saques(*, valor, saldo, LIMITE_SAQUE):

    if valor <= 0:
        print("\n\033[31mO valor do saque deve ser maior que zero!\033[0m\n")
        return True

    elif valor > saldo:
        print("\n\033[31mSaldo insuficiente\033[0m\n")
        return True

    elif valor > LIMITE_SAQUE:
        print("\n\033[31mLimite máximo por operação: R$ 500,00\033[0m\n")
        return True

    return False
