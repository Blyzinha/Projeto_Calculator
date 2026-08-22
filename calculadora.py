#Importando a operação logaritmo

import math

#Criei um def para evitar quebras no código

def pedir_numero(mensagem):
   while True:
      try:
         return float(input(mensagem))
      except ValueError:
         print("Digite apenas números!")

#Criei outro def para pedir operação de jeito mais amplo

def pedir_operacao():
   while True:
      operacao = input("Digite a operação (+, -, *, /, log, ^): ").lower()

      if operacao in ["+", "-", "*", "/", "log", "^"]:
         return operacao

      print("Operação inválida!")

#Criei outro def para calcular

def calcular(num1, operacao, num2):

   if operacao == "+":
      return num1 + num2

   elif operacao == "-":
      return num1 - num2

   elif operacao == "*":
      return num1 * num2

   elif operacao == "/":
      if num2 == 0:
         print("Divisão por zero não é permitida.")
         return None

      return num1 / num2

   elif operacao == "^":
      return num1 ** num2

   elif operacao == "log":

      if num1 <= 0:
         print("O número deve ser maior que 0.")
         return None

      elif num2 <= 0 or num2 == 1:
         print("A base deve ser maior que 0 e diferente de 1.")
         return None

      return math.log(num1, num2)

#Dando titulo à calculadora

print("===============- Calculadora -===============")

#Adicionei vários prints vazios para dar espaço

print()

#Tabela de operações para deixar mais informativo

print("""Operações:

- Adição (+)
- subtração (-)
- Multiplicação (*)
- Divisão (/)
- Logaritmo (log)
- Potenciação (^)""")

print()
print("==============================================")
print()

#Pedindo informações fora do loop

nome = input("Digite seu nome: ")

#Colocando loop para permitir que o usuário faça mais operações

while True:

   num1 = pedir_numero("Digite o primeiro número: ")

   operacao = pedir_operacao()

   num2 = pedir_numero("Digite o segundo número: ")

   resultado = calcular(num1, operacao, num2)

   if resultado is None:
      continue

#Mostrando resultado

   print()
   print(f"Olá, {nome}!")
   print(f"{num1} {operacao} {num2} = {resultado}")

#Sistema para descobrir se é impar ou par e evitando números não inteiros

   if resultado.is_integer():
      if int(resultado) % 2 == 0:
         print("O resultado é Par")
      else:
         print("O resultado é Ímpar")
   else:
      print("O resultado não é um número inteiro.")

   print()
#Quebrando o loop
   continuar = input("Deseja realizar outra operação? (s/n): ")

   if continuar.lower() != "s":
      print("Calculadora encerrada.")
      break
