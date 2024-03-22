numero = 0
inverso = 0

numero = int(input("Digite um número inteiro de 4 dígitos: "))
while numero != 0:
  digito = numero % 10
  inverso = inverso * 10 + digito
  numero = numero // 10

print("Prof inverso", inverso)