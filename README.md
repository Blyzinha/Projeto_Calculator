# Projeto Calculadora

## Sobre o projeto

Este projeto consiste em uma calculadora desenvolvida em Python. A proposta foi criar uma calculadora que, além de realizar as operações matemáticas básicas, como adição, subtração, multiplicação e divisão, também fosse capaz de realizar operações de potenciação e logaritmo.

Além das operações matemáticas, implementei um sistema que verifica o resultado final de cada cálculo e informa se o número obtido é par ou ímpar. Dessa forma, o projeto reúne diferentes conceitos que aprendi em Python, como operações matemáticas, entrada de dados, estruturas condicionais e manipulação de resultados.

## Explicação do código 

Foram utilizadas funções para organizar o código e evitar repetições. A função `pedir_numero()` valida os números digitados pelo usuário, enquanto `pedir_operacao()` verifica se a operação escolhida é válida. A função `calcular()` realiza a operação selecionada e trata erros, como divisão por zero e valores inválidos para logaritmos.

O programa utiliza um `while` para permitir várias operações, `try/except` para evitar erros na entrada de dados e `if/elif` para selecionar os cálculos. Após cada operação, também verifica se o resultado é um número inteiro, identificando se ele é par ou ímpar.

## Funcionalidades

- Adição, subtração, multiplicação, divisão, potenciação e logaritmo.
- Validação de números e operações.
- Tratamento de divisão por zero.
- Verificação de resultados pares e ímpares.
- Possibilidade de realizar várias operações em sequência.

## Como executar o programa

### 1. Dê permissão ao arquivo com o comando:

```bash
chmod +x script_calculadora.sh
```
### 2. Execute o arquivo com:
```bash
./script_calculadora.sh
```
O script irá iniciar o programa `calculadora.py`
