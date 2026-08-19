import math
print("================- Calculadora -================")

#pegando informação do usuario
nome = input("Digite seu nome: ")

#while para ativar o modo de repetição
while True:
   num1 = float(input("Digite o primeiro número: "))
   operacao = input("Digite a operação (+, -, *, /, log, ^): ")
   num2 = float(input("Digite o segundo número: "))

#Estrutura condicional para calcular os números
   if operacao == "+":
      resultado = num1 + num2
   elif operacao == "-":
      resultado = num1 - num2
   elif operacao == "*":
      resultado = num1 * num2
   elif operacao == "/":
      if num2 != 0:
         resultado = num1 / num2
      else:
         print("Divisão por zero não é permitida, Tente novamente.")
         continue
   elif operacao == "log":
      resultado = math.log(num1, num2)
   elif operacao == "^":
      resultado = num1 ** num2
   else:
      print("Operação inválida.")
      continue
   
   print("")

#mostrando o resultado
   print(f"Olá, {nome}! Seu resultado é: {num1} {operacao} {num2} = {resultado}")

#sistema para identificar se o resultado é ímpar ou par

   if resultado % 2 == 0:
      print("O resultado final é Par")
   else:
      print("O resultado final é Ímpar")

   print("")

#agora quebrei o ciclo

   continuar = input("Deseja realizar outra operação? (s/n): ")
   if continuar.lower() != "s":
      break


