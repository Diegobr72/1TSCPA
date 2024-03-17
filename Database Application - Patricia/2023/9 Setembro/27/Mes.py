#(aula 5)Escreva um programa que pergunte em qual mês estamos (1-12) e ao final utilize uma estrutura de decisão por seleção para escrever o nome do mês por extenso na tela.

titulo = "Programa do Mês"
print(f'{titulo:^30}')

mes = int(input("Entre com um número de 1-12: "))

if 1 <= mes <= 12:
    if mes == 1:
        print("Janeiro")
    elif mes == 2:
        print("Fevereiro")
    elif mes == 3:
        print("Março")
    elif mes == 4:
        print("Abril")
    elif mes == 5:
        print("Maio")
    elif mes == 6:
        print("Junho")
    elif mes == 7:
        print("Julho")
    elif mes == 8:
        print("Agosto")
    elif mes == 9:
        print("Setembro")
    elif mes == 10:
        print("Outubro")
    elif mes == 11:
        print("Novembro")
    elif mes == 12:
        print("Dezembro")
else:
    print("Mês inválido")
