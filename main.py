class Conta:
    def __init__(self, saldo_inicial=1500):
        self.saldo = saldo_inicial
        self.extratos = []
        self.depositos = []
        self.saques = []
        self.saque_diario = 3
        self.saque_dia = 0
        self.limite_maximo = 500
        self.limite_maximo_saque = 1500
        self.total_saque = 0


# Depósito
# Deve ser possível depositar valores positivos para a conta bancária.
# A versão 1 do projeto trabalha apenas com 1 usuário, portanto não é necessário identificar número de agência ou conta.
# Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

    def deposito(self, valor):

        deposito_negativo = valor <= 0

        if deposito_negativo:
            print("O valor do depósito não pode ser negativo!")

        else:

            self.depositos.append(valor)
            self.saldo += valor

            mensagem_extrato = f"Depósito R$ {valor:.2f}"
            self.extratos.append(mensagem_extrato)

            mensagem_deposito = f"Depósito de {valor:.2f} realizado com sucesso!"

            print()
            largura = len(mensagem_deposito) + 10
            print("-" * largura)
            print(mensagem_deposito.center(largura))
            print("-" * largura)
            print()


# Saque
# O sistema deve permitir realizar 3 saques diários, com limite máximo de R$ 500,00 por saque.
# Caso o usuário não tenha saldo, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
# Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato


    def saque(self, valor):

        if valor > self.saldo:
            print("\n\033[31mSaldo insuficiente\033[0m\n")

        elif self.saque_dia == self.saque_diario:
            print("\nSaque diário Excedido\n")

        elif valor > self.limite_maximo:
            print("\nLimite máximo por operação: R$ 500,00\n")

        elif self.total_saque + valor > self.limite_maximo_saque:
            print("\nLimite total de saque atingido: R$ 1500,00\n")

        else:

            self.total_saque += valor
            self.saque_dia += 1
            self.saldo -= valor
            self.saques.append(valor)

            mensagem_extrato = f"Saque R$ {valor:.2f}"
            self.extratos.append(mensagem_extrato)

            mensagem_saque = f"Saque de {valor:.2f} realizado com sucesso!"

            print()
            largura = len(mensagem_saque) + 10
            print("-" * largura)
            print(mensagem_saque.center(largura))
            print("-" * largura)
            print()

    # Extrato
    # Essa operação deve listar todos os depósitos e saques realizados na conta.
    # No fim da listagem deve ser exibido o saldo atual da conta.
    # Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
    # 1500.45 = R$ 1500.45

    def extrato(self):

        mensagem_extrato = "EXTRATO"

        print()
        largura = 50
        print("-" * largura)
        print(mensagem_extrato.center(largura))
        print("-" * largura)

        for i in self.extratos:
            tipo = i.split()

            operacao = tipo[0].ljust(10)
            valor = " ".join(tipo[1:3]).rjust(40)

            largura = 50
            print(operacao + valor)
            print("-" * largura)

        saldo = f"{self.saldo:.2f}"
        saldo_atual = "Saldo".ljust(10) + f"R$ {saldo}".rjust(40)
        print(saldo_atual)
        print()

    def menu(self):

        sistema = "SISTEMA BANCÁRIO"

        largura = 50
        print("=" * largura)
        print(sistema.center(largura))
        print("=" * largura)
        print()

        while True:

            print(
                "Digite (1) Depósito: (2) Saque: (3) Extrato: (4) Sair: ")

            opcao = input("Opção: ")
            print()

            opcao_1 = opcao == "1"
            opcao_2 = opcao == "2"
            opcao_3 = opcao == "3"
            opcao_4 = opcao == "4"

            if opcao_1:

                try:
                    valor = float(input("Digite o valor de depósito: R$ "))
                    self.deposito(valor)
                except ValueError:
                    print("\n\33[31mEntrada Inválida!\33[0m\n")

            elif opcao_2:
                mensagem_1 = "Limite máximo por operação: R$ 500,00"
                mensagem_2 = "Limite total de saque: R$ 1.500,00"
                mensagem_3 = "Limite de saques diários: 3"

                largura = max(len(mensagem_1), len(
                    mensagem_2), len(mensagem_3)) + 10
                print("=" * largura)
                print(mensagem_1.center(largura))
                print(mensagem_2.center(largura))
                print(mensagem_3.center(largura))
                print("=" * largura)

                try:
                    valor = float(input("\nDigite o valor do saque: R$ "))
                    self.saque(valor)
                except ValueError:
                    print("\n\33[31mEntrada Inválida!\33[0m\n")

            elif opcao_3:
                self.extrato()

            elif opcao_4:
                break

            else:
                print("Opção Inválida!\n")


minha_conta = Conta()
minha_conta.menu()
