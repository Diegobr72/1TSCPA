numero = int(input("Entre com um numero de 4 digitos:"))
inteira = numero // 1000
resto = numero % 1000
numero = resto
milhar = inteira

inteira = numero // 100
resto = numero % 100
numero = resto
centena = inteira

inteira = numero // 10
resto = numero % 10
numero = resto
dezena = inteira
unidade = resto

numero_invertido = str(unidade) + str(dezena) + str(centena) + str(milhar)
print(numero_invertido)

numero_invertido = unidade * 1000 + dezena * 100 + centena * 10 + milhar

print(numero_invertido)