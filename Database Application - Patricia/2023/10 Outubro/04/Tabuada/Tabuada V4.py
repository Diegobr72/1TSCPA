print("Tabuada com o FOR")
numero = int(input("Qual tabuada deseja calcular? "))
print("Com o range 11 e primeiro 1")
for i in range(1,11):
  tabuada = numero * i
  print(numero, "X", i, "=", tabuada)