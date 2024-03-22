numero = int(input("Digite um número inteiro de 4 dígitos: "))
if 1000 <= numero <= 9999:

    d1 = numero % 10 #6
    numero = numero // 10
    inverso = d1 #6

    d2 = numero % 10 #7
    inverso = inverso *10  + d2 #6*10 +7 = 67

    numero = numero // 10
    d3 = numero % 10 # 8

    inverso = inverso * 10 + d3 # 67 *10 + 8 = 678
    d4 = numero // 10
    inverso = inverso * 10 + d4 # 678 * 10 + 9 = 6789

    numero_invertido = d1 * 1000 + d2 * 100 + d3 * 10 + d4
