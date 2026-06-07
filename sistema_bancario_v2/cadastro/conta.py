from funcoes_validacao.validacoes import verificar_duplicidade_conta


def cadastrar_nova_conta(contas, numero_conta, /, *, cpf, AGENCIA):

    nova_conta_numero = numero_conta[-1] + 1 if numero_conta else 1

    cadastro_conta = {
        "agencia": AGENCIA,
        "conta": nova_conta_numero,
        "cpf": cpf
    }

    if not verificar_duplicidade_conta(cadastro_conta, contas):

        contas.append(cadastro_conta)
        numero_conta.append(nova_conta_numero)

        print("\n\033[32mConta Cadastrada com sucesso!\033[0m\n")
        print(f"Agência: {contas[-1]['agencia']}")
        print(f"Conta: {contas[-1]['conta']}")
        print(f"CPF: {contas[-1]['cpf']}\n")

    else:
        print("Conta já cadastrada")
        return False

    return contas
