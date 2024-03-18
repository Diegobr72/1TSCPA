print("Pares e Impares entre dois numeros")

n1 = int(input("Entre com o primeiro numero: "))
n2 = int(input("Entre com o segundo numero: "))

if n1 > n2:
  aux = n1
  n1 = n2
  n2 = aux

i = n1
qp, qi = 0, 0
#7 e 10 há 2 números pares e 2 números ímpares
#7 8 9 10#
while i <= n2:
  if i % 2 == 0:
    qp += 1
    print(f'{i} é par')
  else:
    qi += 1
    print(f'{i} é ímpar')
  i += 1
print(f'Temos {qp} numeros pares e {qi} numeros impares')
