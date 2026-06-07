from datetime import datetime


def depositar(valor, saldo, extrato, /):

    saldo += valor

    data_atual = datetime.now()
    data_hora_operacao = data_atual.strftime("%d/%m/%Y %H:%M")

    mensagem_extrato = f"Depósito R$ {valor:.2f} {data_hora_operacao}"
    extrato.append(mensagem_extrato)

    mensagem_deposito = f"Depósito de {valor:.2f} realizado com sucesso!"
    print()
    largura = len(mensagem_deposito) + 10
    print("-" * largura)
    print(mensagem_deposito.center(largura))
    print("-" * largura)
    print()

    return saldo, extrato


def sacar(*, valor, saldo, qtde_saques, extrato):

    saldo -= valor
    qtde_saques += 1

    data_atual = datetime.now()
    data_hora_operacao = data_atual.strftime("%d/%m/%Y %H:%M")
    mensagem_extrato = f"Saque R$ {valor:.2f} {data_hora_operacao}"
    extrato.append(mensagem_extrato)

    mensagem_saque = f"Saque de {valor:.2f} realizado com sucesso!"
    print()
    largura = len(mensagem_saque) + 10
    print("-" * largura)
    print(mensagem_saque.center(largura))
    print("-" * largura)
    print()

    return saldo, extrato, qtde_saques


def exibir_extrato(saldo, /, *, extrato):

    mensagem_extrato = "EXTRATO"
    print()
    largura = 50
    print("-" * largura)
    print(mensagem_extrato.center(largura))
    print("-" * largura)

    for transacao in extrato:
        tipo = transacao.split()

        operacao = tipo[0].ljust(10)
        valor = f"{tipo[1]} {tipo[2]}".rjust(20)
        data_hora_realizacao = " ".join(tipo[3:]).rjust(20)

        largura = 50
        print(operacao + valor + data_hora_realizacao)
        print("-" * largura)

    saldo = f"{saldo:.2f}"
    saldo_atual = "Saldo".ljust(10) + f"R$ {saldo}".rjust(40)
    print(saldo_atual)
    print()
