print("Aprovado na faculdade?")
media = float(input("Entre com a sua media anual: "))
if media < 0 or media > 10:
  print("Media invalida")
else:
  if media >= 6:
    print("Aprovado")
  elif media >= 4:
    print("Exame")
  else:
    print("Reprovado")