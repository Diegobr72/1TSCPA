print("Acordo da Damp")
dia = int(input("Qual o dia da semana (1- domingo, 7-sabado)? "))
if dia == 6:
  licao = input("Voce fez a licao de casa? ").lower().strip()
  banho = input("Voce deu banho no SNIFF? ").lower().strip()
  if licao in ('sim', 's', 'yes', 'y') and banho in ('sim', 's', 'yes', 'y'):
    print("Oba vamos tomar sorvete na DAMP")
  else:
    if licao not in ('sim', 's', 'yes', 'y') and banho not in ('sim', 's', 'yes', 'y'):
      print("Voce deve fazer a licao e lavar o cachorro")
    elif licao not in ('sim', 's', 'yes', 'y'):
      print("Voce deve fazer a licao")
    else:
      print("Voce deve dar banho no Sniff")
else:
  print("So vamos tomar sorvete na sexta")