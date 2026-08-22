# Projeto Calculadora

## Sobre o projeto

Este projeto consiste em uma calculadora desenvolvida em Python. A proposta foi criar uma calculadora que, além de realizar as operações matemáticas básicas, como adição, subtração, multiplicação e divisão, também fosse capaz de realizar operações de potenciação e logaritmo.

Além das operações matemáticas, implementei um sistema que verifica o resultado final de cada cálculo e informa se o número obtido é par ou ímpar. Dessa forma, o projeto reúne diferentes conceitos que aprendi em Python, como operações matemáticas, entrada de dados, estruturas condicionais e manipulação de resultados.

## Explicação do código 

- Primeiro, utilizei `import math` para ter acesso às funções matemáticas necessárias para realizar o cálculo de logaritmos.
- Depois, utilizei um loop `while` para permitir que a calculadora continue funcionando e realizando novos cálculos enquanto o usuário desejar. Dentro desse loop, também são solicitados os números que serão utilizados nas operações, usando `input()`.
- Utilizei estruturas condicionais para identificar qual operação matemática o usuário deseja realizar, executar o cálculo correspondente e evitar possíveis erros que poderiam interromper a execução do programa.
- Por fim, adicionei uma estrutura responsável por verificar se o resultado obtido é um número par ou ímpar. Depois disso, utilizei o comando `print()` para exibir o resultado do cálculo e informar ao usuário se o número é par ou ímpar.

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
