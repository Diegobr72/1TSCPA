print("Fibonacci")
termo = int(input("Até que termo queremos calcular a sequencia de Fibonacci? "))
#a = 0
#b = 1
# esse comando equivale ao anterior
a, b = 0, 1

if termo <= 0:
  print("Numero de termos inválidos")
elif termo > 1:
  print(a, b, end = " ")
  i = 2
  while i < termo:
    fibo = a + b
    print(fibo, end = " ")
    a = b
    b = fibo
    i += 1
    #i = i + 1
  print("\n")
else:
  print(a)