#Versao gerada pela IA com o FOR
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

pares = 0
impares = 0

for i in range(n1, n2 + 1):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1