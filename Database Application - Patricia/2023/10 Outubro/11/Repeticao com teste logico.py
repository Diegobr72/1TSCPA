# Estrutura de repeticao com teste logico

#Estrutura de repeticao com o FOR
numero = int(input("Qual tabuada deseja calcular? "))
for i in range(1, 11):
  tabuada = numero * i
  print(numero, "X", i, "=", tabuada)


#Estrutura de repeticao com o WHILE
numero = int(input("Qual tabuada deseja calcular? "))
#inicializa a variavel contadora i, com o valor inicial
i = 1
#a comparacao é feita no while, é similar ao if
while i <= 10:
  tabuada = numero * i
  print(numero, "X", i, "=", tabuada)
  #nos, desenvolvedores é que somos responsáveis por fazer o incremento do contador
  #i = i + 1
  i += 1