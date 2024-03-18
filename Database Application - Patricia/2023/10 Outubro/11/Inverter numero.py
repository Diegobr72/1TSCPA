numero = input("Digite um número de 4 dígitos: ")

if len(numero) != 4:
    print("O número deve conter exatamente 4 dígitos.")
else:

    d1 = numero[0]
    d2 = numero[1]
    d3 = numero[2]
    d4 = numero[3]

    ni = d4 + d3 + d2 + d1

    print("Número invertido:", ni)