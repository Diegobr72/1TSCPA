print("Está em dúvida se algum número entre os seus é divisível por 5?")
print("Eu posso te ajudar!")

A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))

if B > A:
    dominante = B
    inicio = A
else:
    dominante = A
    inicio = B

for numero in range(inicio, dominante + 1):
    if numero % 5 == 0:
        print(numero)