print('''calculadora python
1 adiçao
2 subtraçao
3 multiplicaçao
4 divisao ''')
opçao = int(input("digite uma opçao: "))
if opçao == 1:
  num1 = int(input("digite o valor 1: "))
  num2 = int(input("digite o valor 2: "))
  soma = num1 + num2
  print("resltado: ",(soma))
  
elif opçao == 2:
  num1 = int(input("digite o valor 1: "))
  num2 = int(input("digite o valor 2: "))
  sub = num1 - num2
  print("resltado: ",(sub))
elif opçao == 3:
  num1 = int(input("digite o valor 1: "))
  num2 = int(input("digite o valor 2: "))
  mult = num1 * num2
  print("resltado: ",(mult))
elif opçao == 4:
  num1 = int(input("digite o valor 1: "))
  num2 = int(input("digite o valor 2: "))
  div = num1 / num2
  print("resltado: ",(div))
else:
  print("selecionar apenas 1 a 4")
