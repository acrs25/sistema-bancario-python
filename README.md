# 🏦 Sistema Bancário em Python

Projeto evolutivo de um sistema bancário desenvolvido em Python, com foco em boas práticas de programação, modularização e versionamento.

---

## 🚀 Versão 1.0.0 — Operações Bancárias Básicas
**Release:** [v1.0.0](https://github.com/acrs25/sistema-bancario-python/releases/tag/v1.0.0)

### 🧩 Características
- Implementação orientada a objetos (POO)
- Operações: **Depósito**, **Saque** e **Extrato**
- Limite de **3 saques diários** e **R$ 500,00 por saque**
- Exibição de saldo formatado em `R$ xxx.xx`
- Projeto voltado para **um único usuário**

### 📜 Regras da Versão 1
1. Depósitos aceitam apenas valores positivos.  
2. Saques limitados a 3 por dia e R$ 500,00 por operação.  
3. Extrato lista todas as transações e mostra o saldo final.  
4. Não há cadastro de usuários ou contas — apenas uma conta única.  

---

## 🧭 Versão 2.0.0 — Sistema Bancário Modularizado
**Release:** [v2.0.0](https://github.com/acrs25/sistema-bancario-python/releases/tag/v2.0.0)

### 🧩 Características
- Código **modularizado** com separação em pacotes e funções:
  - `banco_logica/` → operações bancárias  
  - `cadastro/` → usuários e contas  
  - `funcoes_validacao/` → validações e regras de negócio  
- Registro de **data e hora** em todas as transações  
- Limite de **10 transações diárias por conta**  
- Funções novas:
  - `criar_usuario()` → cadastra cliente com nome, CPF, data de nascimento e endereço  
  - `cadastrar_nova_conta()` → vincula conta ao usuário  
- Validação de CPF e prevenção de duplicidade de contas  
- Suporte a múltiplos usuários e múltiplas contas  

### 📜 Regras da Versão 2
1. Separar todas as operações em funções (`depositar`, `sacar`, `exibir_extrato`).  
2. Criar funções para **cadastro de usuário** e **cadastro de conta corrente**.  
3. Limitar o número de transações diárias a **10 por conta**.  
4. Exibir **data e hora** de cada operação no extrato.  
5. Garantir que não existam dois usuários com o mesmo CPF.  
6. Cada conta pertence a um único usuário, mas um usuário pode ter várias contas.  

---

## 📊 Comparativo entre Versões

| Aspecto                  | Versão 1.0.0 (POO) | Versão 2.0.0 (Modular) |
|---------------------------|--------------------|------------------------|
| Arquitetura              | Orientada a Objetos | Modularizada em pacotes |
| Usuários                 | Apenas 1           | Múltiplos usuários      |
| Contas                   | Única conta        | Várias contas por usuário |
| Limite de transações     | 3 saques/dia       | 10 transações/dia       |
| Registro de data/hora    | Não                | Sim                     |
| Validação de CPF         | Não                | Sim                     |
| Extrato                  | Simples            | Completo com data/hora  |

---

## 🧠 Objetivo do Projeto
Demonstrar a evolução de um sistema bancário simples para uma arquitetura mais robusta e escalável, aplicando:
- Orientação a objetos (v1)  
- Modularização e funções com diferentes tipos de argumentos (v2)  
- Validação de dados  
- Boas práticas de versionamento e documentação  

---

## 📦 Execução
```bash
python main.py
