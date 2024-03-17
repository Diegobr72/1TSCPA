print("Tabuada com o FOR")
numero = int(input("Qual tabuada deseja calcular? "))
print("Com o range e pulo de 2")
for i in range(1,11,2):
  tabuada = numero * i
  print(numero, "X", i, "=", tabuada)