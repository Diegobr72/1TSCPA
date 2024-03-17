print("Programa para cálculo de ticket de estacionamento")
horas = int(input("Digite quantas você horas ficou?"))
if 1 <= horas <= 6:
    preco = horas * 5
    print("O valor a ser pago do seu ticket é R$", preco, "!")
elif horas >= 7:
    print("O valor a ser pago do seu ticket é R$ 35,00!")
else:
    print("digite um valor valido")