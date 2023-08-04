class calculadora:
   v1 = int(input("Digite o primeiro numero: "))
   v2 = int(input("Digite o segundo numero: "))

   operacao = input("Digite * ou / ")

   multiplique = v1*v2

   divide = v1/v2

   if operacao == '*':
      print(v1, '*', v2, '=', multiplique)
   elif operacao == '/':
      print(v1, '/', v2, '=', divide)