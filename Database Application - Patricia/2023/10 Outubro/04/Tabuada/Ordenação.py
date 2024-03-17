print("Ordenacao")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
print("a: ", a, "b: ", b)
# if 90 > 7
if a > b:
    # aux = 7
    aux = b

    # b(valor antigo 7) = 90
    b = a

    # a(valor antigo 90) = 7(valor q estava no aux)
    a = aux
print("a: ", a, "b: ", b)

for i in range(a, b + 1):
    if i % 5 == 0:
        print(i)