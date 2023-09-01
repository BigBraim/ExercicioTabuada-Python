class tabuada1:
   numero = int(input("Digite um número: "))

   operacao = input("Digite * ou /: ")


   for tabuada in range(1, 11):


      if operacao == '*':
         print(numero,'*',tabuada,'=',numero * tabuada)
      elif operacao == '/':
         print(numero, '/', tabuada, '=', numero / tabuada)
