import re


def criar_usuario(nome, data_nasc, endereco, clientes, /, *, cpf):

    data_nasc = re.sub(r"\D", "-", data_nasc)
    cpf = re.sub(r"\D", "", cpf)

    cliente = {
        "nome": nome,
        "data_nasc": data_nasc,
        "endereco": endereco,
        "cpf": cpf
    }

    clientes.append(cliente)

    print("\n\033[32mCliente Cadastrado com Sucesso!\033[0m\n")

    return clientes
