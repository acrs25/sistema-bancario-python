from banco_logica.operacoes import depositar, sacar, exibir_extrato
from cadastro.usuarios import criar_usuario
from cadastro.conta import cadastrar_nova_conta
from funcoes_validacao.validacoes import (
    verificar_cpf, verificar_limite_transacoes,
    verificar_restricao_deposito,
    verificar_restricao_saques,
    verificar_saques_dia)


def menu():
    sistema = "SISTEMA BANCÁRIO"

    largura = 50
    print("=" * largura)
    print(sistema.center(largura))
    print("=" * largura)
    print()

    print("""
    (1) Depósito
    (2) Saque
    (3) Extrato
    (4) Cadastro Cliente
    (5) Cadastro Conta
    (6) Sair
            """)

    return input("Digite uma Opção: ")


def main():

    clientes = []
    numero_conta = []
    contas = []

    AGENCIA = "001"
    saldo = 0
    extrato = []
    qtde_saques = 0
    SAQUES_DIARIOS = 3
    LIMITE_SAQUE = 500
    LIMITE_TRANSACOES_DIARIAS = 10

    while True:

        opcao = menu()

        escolheu_deposito = opcao == "1"
        escolheu_saque = opcao == "2"
        escolheu_extrato = opcao == "3"
        cadastrar_cliente = opcao == "4"
        cadastrar_conta = opcao == "5"
        escolheu_sair = opcao == "6"

        if escolheu_deposito:
            if verificar_limite_transacoes(LIMITE_TRANSACOES_DIARIAS, extrato):
                continue

            try:
                valor = float(
                    input("\nDigite o valor de depósito: R$ ").replace(",", "."))

                if verificar_restricao_deposito(valor=valor):
                    continue

                saldo, extrato = depositar(valor, saldo, extrato)

            except ValueError:
                print("\n\33[31mEntrada Inválida!\33[0m\n")

        elif escolheu_saque:
            if verificar_limite_transacoes(LIMITE_TRANSACOES_DIARIAS, extrato):
                continue

            if verificar_saques_dia(qtde_saques=qtde_saques,
                                    SAQUES_DIARIOS=SAQUES_DIARIOS):
                continue

            mensagem_1 = f"Limite máximo por operação: R$ {LIMITE_SAQUE:.2f}"
            mensagem_2 = f"Limite de saques diários: {SAQUES_DIARIOS}"

            print()
            largura = max(len(mensagem_1), len(
                mensagem_2)) + 10
            print("=" * largura)
            print(mensagem_1.center(largura))
            print(mensagem_2.center(largura))
            print("=" * largura)
            print()

            try:
                valor = float(
                    input("Digite o valor do saque: R$ ").replace(",", "."))

                if verificar_restricao_saques(valor=valor,
                                              saldo=saldo,
                                              LIMITE_SAQUE=LIMITE_SAQUE):
                    continue

                saldo, extrato, qtde_saques = sacar(valor=valor,
                                                    saldo=saldo,
                                                    qtde_saques=qtde_saques,
                                                    extrato=extrato)

            except ValueError:
                print("\n\33[31mEntrada Inválida!\33[0m\n")

        elif escolheu_extrato:
            exibir_extrato(saldo, extrato=extrato)

        elif cadastrar_cliente:

            cpf = input("\nDigite seu CPF (somente numeros): ")

            if cpf.isdigit():
                if verificar_cpf(clientes, cpf=cpf):
                    print("\n\033[31mCliente já cadastrado!\033[0m\n")
                    continue

                nome = input("\nDigite o seu nome: ")
                data_nasc = input(
                    "\nDigite sua data de nascimento (dd/mm/aa): ")

                endereco = input(
                    "\nDigite seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

                clientes = criar_usuario(
                    nome, data_nasc, endereco, clientes, cpf=cpf)

            else:
                print(
                    "\n\033[31mCPF inválido - Digite apenas números.\033[0m\n")

        elif cadastrar_conta:

            cpf = input("\nInforme o número do CPF: ")

            if cpf.isdigit():
                if not verificar_cpf(clientes, cpf=cpf):
                    print(
                        "\n\033[31mCPF não encontrado. Realize o cadastro do Cliente!\033[0m\n")
                    continue

                contas = cadastrar_nova_conta(contas, numero_conta,
                                              cpf=cpf,
                                              AGENCIA=AGENCIA
                                              )

            else:
                print(
                    "\n\033[31mCPF inválido - Digite apenas números.\033[0m\n")

        elif escolheu_sair:
            print("\n\033[31mSaindo do sistema...\033[0m\n")

            break
        else:
            print("\n\033[31mOpção Inválida!\033[0m\n")


if __name__ == "__main__":
    main()
