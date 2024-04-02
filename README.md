# Sistema Bancário em Python
Este é um sistema bancário simples implementado em Python, conforme o desafio proposto pela DIO (Digital Innovation One). O programa permite realizar operações de depósito, saque e exibir o extrato da conta.

## Funcionalidades

**1. Depósito (d):**
- Solicita ao usuário o valor a ser depositado.
- Verifica se o valor é válido (maior que zero).
- Atualiza o saldo e registra a operação no extrato.

**2. Saque (s):**
- Verifica se o limite diário de saques não foi excedido (3 saques por dia).
- Solicita ao usuário o valor a ser sacado.
- Verifica se o valor é válido (maior que zero, dentro do limite de saque e com saldo suficiente).
- Atualiza o saldo e registra a operação no extrato.

**3. Extrato (e):**
- Exibe todas as operações de depósito e saque realizadas.
- Caso não haja movimentações, exibe a mensagem “Não foram realizadas movimentações”.
- Mostra o saldo atual.

## Regras

1. Todas as operações de depósito e saque são armazenadas em uma variável chamada `extrato`.
2. O limite diário de saques é de 3 operações.
3. O saldo inicial é zero, e o limite de saque é de R$ 500.

## Executando o Programa

1. Execute o código Python.
2. Escolha a operação desejada digitando a letra correspondente (**d** para **depósito**, **s** para **saque**, **e** para **extrato** ou **q** para **sair**).
3. Siga as instruções para realizar as operações.
