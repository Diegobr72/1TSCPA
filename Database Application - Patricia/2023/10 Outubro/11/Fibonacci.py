# Escreva um algoritmo que solicite um número ao usuário. Este número será o N-ésimo termo da série de Fibonacci. A sequência de Fibonacci é uma sequência numérica iniciada por 0 e 1. Os demais termos são dados pela soma dos dois termos anteriores.
# Exemplo: 0,1,1,2,3,5,8,13,21

# Se eu falar numero 3, a sequencia de fibo exibida deveria ser
# 0, 1, 1

# Se eu falar numero 6, a sequencia de fibo exibida deveria ser
# 0, 1, 1, 2, 3, 5

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